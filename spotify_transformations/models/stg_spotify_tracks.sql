-- silver model 

{{ config(
    materialized='table',
    format='parquet'
) }}

SELECT 
    t.element.id AS track_id,
    t.element.name AS track_name,
    t.element.artists[1].name AS primary_artist,
    t.element.album.name AS album_name,
    t.element.duration_ms AS duration_ms,
    t.element.popularity AS popularity,
    t.element.album.release_date AS release_date
FROM 
    "spotify_data_catalog"."raw",  
    UNNEST(items) AS t(element)