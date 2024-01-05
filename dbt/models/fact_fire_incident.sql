WITH incident_cte AS (
    SELECT
        incident_id,
        date_column,
        district,
        battalion
    FROM
        {{ source('incidents', 'raw_incidents') }}
)

SELECT
    incident_id,
    dim_date.id AS date_id,
    district,
    battalion
FROM incident_cte
JOIN {{ ref('dim_date') }} ON incident_cte.date_column = dim_date.date;