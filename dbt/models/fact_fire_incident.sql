WITH incident_cte AS (
    SELECT
        id,
        incident_date,
        city,
        zipcode,
        station_area,
        battalion
    FROM
        {{ source('incidents', 'raw_incidents') }}
)

SELECT
    *
FROM incident_cte