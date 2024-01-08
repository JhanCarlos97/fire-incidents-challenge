-- models/aggregated_district.sql

WITH district_aggregation AS (
    SELECT
        city,
        zipcode,
        station_area,
        COUNT(*) AS incident_count
    FROM
        {{ source('incidents', 'raw_incidents') }}
    GROUP BY
        1, 2, 3
)

SELECT
    city,
    zipcode,
    station_area,
    incident_count
FROM
    district_aggregation