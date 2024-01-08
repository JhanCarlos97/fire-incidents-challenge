-- models/aggregated_time_period.sql

WITH time_aggregation AS (
    SELECT
        date_trunc('day', incident_date) AS day,
        date_trunc('month', incident_date) AS month,
        date_trunc('year', incident_date) AS year,
        COUNT(*) AS incident_count
    FROM
        {{ source('incidents', 'raw_incidents') }}
    GROUP BY
        1, 2, 3
)

SELECT
    day,
    month,
    year,
    incident_count
FROM
    time_aggregation