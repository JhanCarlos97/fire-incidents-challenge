-- Create necessary tables
CREATE TABLE IF NOT EXISTS raw_incidents (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    district VARCHAR(255),
    battalion VARCHAR(255),
    -- Other columns
);