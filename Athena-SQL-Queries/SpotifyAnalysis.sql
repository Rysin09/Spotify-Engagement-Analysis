SELECT * FROM spotify_history LIMIT 20;

SELECT 
    ROUND(SUM(play_minutes) / 60, 2) AS total_hours
FROM spotify_history;

SELECT 
    artist, 
    ROUND(SUM(play_minutes), 2) AS minutes
FROM spotify_history
GROUP BY artist
ORDER BY minutes DESC
LIMIT 10;

SELECT 
    track, 
    artist,
    ROUND(SUM(play_minutes), 2) AS minutes
FROM spotify_history
GROUP BY track, artist
ORDER BY minutes DESC
LIMIT 10;

SELECT 
    year,
    ROUND(SUM(play_minutes)/60, 2) AS hours
FROM spotify_history
GROUP BY year
ORDER BY year;

SELECT 
    time_of_day,
    ROUND(SUM(play_minutes), 2) AS minutes
FROM spotify_history
GROUP BY time_of_day
ORDER BY minutes DESC;

SELECT 
    day_of_week,
    ROUND(SUM(play_minutes), 2) AS minutes
FROM spotify_history
GROUP BY day_of_week;

SELECT 
    artist,
    COUNT(*) AS plays,
    SUM(CASE WHEN is_skipped THEN 1 END) AS skipped,
    ROUND(SUM(CASE WHEN is_skipped THEN 1 END) * 100.0 / COUNT(*), 2) AS skip_rate
FROM spotify_history
GROUP BY artist
ORDER BY skip_rate DESC
LIMIT 10;
