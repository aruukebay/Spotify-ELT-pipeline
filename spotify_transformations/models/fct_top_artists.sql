-- gold model

{{ config(
    materialized='table',
    format='parquet'
) }}

SELECT 
    primary_artist,
    COUNT(*) AS total_plays,
    AVG(duration_ms) / 1000 AS avg_song_duration_seconds
FROM 
    {{ ref('stg_spotify_tracks') }}
GROUP BY 1
ORDER BY total_plays DESC