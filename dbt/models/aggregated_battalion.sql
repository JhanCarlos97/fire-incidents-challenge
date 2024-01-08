-- models/aggregated_battalion.sql

WITH battalion_aggregation AS (
    SELECT
        battalion,
        COUNT(*) AS incident_count
    FROM
        {{ source('incidents', 'raw_incidents') }}
    GROUP BY
        1
)

SELECT
    battalion,
    incident_count
FROM
    battalion_aggregation