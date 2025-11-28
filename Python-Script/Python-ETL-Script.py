import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql import functions as F

# --------- Args & Context ----------
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# --------- Read from Data Catalog (raw table) ----------
raw_dyf = glueContext.create_dynamic_frame.from_catalog(
    database="spotify_analytics_db",
    table_name="raw"
)

df = raw_dyf.toDF()

# --------- Basic Cleaning ----------
df = df.filter(F.col("ms_played") > 0)
df = df.withColumn("ms_played", F.col("ms_played").cast("long"))
df = df.withColumn("ts", F.col("ts").cast("timestamp"))

# --------- Time Columns ----------
df = (
    df.withColumn("play_timestamp", F.col("ts"))
      .withColumn("play_date", F.to_date("ts"))
      .withColumn("year", F.year("ts"))
      .withColumn("month", F.month("ts"))
      .withColumn("day", F.dayofmonth("ts"))
      .withColumn("hour", F.hour("ts"))
      .withColumn("day_of_week", F.date_format("ts", "E"))
      .withColumn("is_weekend", F.col("day_of_week").isin("Sat", "Sun"))
)

df = df.withColumn(
    "time_of_day",
    F.when((F.col("hour") >= 5) & (F.col("hour") < 12), "Morning")
     .when((F.col("hour") >= 12) & (F.col("hour") < 17), "Afternoon")
     .when((F.col("hour") >= 17) & (F.col("hour") < 22), "Evening")
     .otherwise("Night")
)

# --------- Playback Metrics ----------
df = (
    df.withColumn("play_seconds", F.col("ms_played") / 1000.0)
      .withColumn("play_minutes", F.col("ms_played") / 60000.0)
      .withColumn("is_meaningful_play", F.col("play_seconds") >= 30)
)

# --------- Rename Columns ----------
df = (
    df.withColumnRenamed("spotify_track_uri", "track_uri")
      .withColumnRenamed("track_name", "track")
      .withColumnRenamed("artist_name", "artist")
      .withColumnRenamed("album_name", "album")
      .withColumnRenamed("platform", "platform_name")
      .withColumnRenamed("reason_start", "reason_start_raw")
      .withColumnRenamed("reason_end", "reason_end_raw")
)

df = (
    df.withColumn("is_shuffle", F.col("shuffle").cast("boolean"))
      .withColumn("is_skipped", F.col("skipped").cast("boolean"))
)

# --------- Final Columns ----------
final_cols = [
    "track_uri","track","artist","album","platform_name","ms_played",
    "play_seconds","play_minutes","is_meaningful_play","is_skipped",
    "is_shuffle","reason_start_raw","reason_end_raw","play_timestamp",
    "play_date","year","month","day","hour","day_of_week",
    "is_weekend","time_of_day"
]

df_final = df.select(*final_cols)

# --------- Convert to DynamicFrame ----------
processed_dyf = DynamicFrame.fromDF(df_final, glueContext, "processed_dyf")

# --------- Write to S3 ----------
output_path = "s3://aryan-spotify-datalake/processed/spotify_history/"

glueContext.write_dynamic_frame.from_options(
    frame=processed_dyf,
    connection_type="s3",
    connection_options={"path": output_path, "partitionKeys": ["year", "month"]},
    format="parquet"
)

job.commit()

