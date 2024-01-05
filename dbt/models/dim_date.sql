-- Create a dimension table for dates
WITH date_cte AS (
    SELECT
        DISTINCT date_column AS date,
        EXTRACT(year FROM date_column) AS year,
        EXTRACT(month FROM date_column) AS month,
        EXTRACT(day FROM date_column) AS day,
        -- Add more date-related attributes as needed
    FROM
        {{ source('incidents', 'raw_incidents') }}
)

SELECT
    date,
    year,
    month,
    day
    -- Add more columns as needed
FROM date_cte;