import requests
from scripts.utils.connect_to_db import connect_to_postgre

def ingest_incidents_data():

    # Read the SQL statement from the file
    with open('insert_raw_incidents_data.sql', 'r') as sql_file:
        insert_sql = sql_file.read()

    # Fetch data from the API endpoint
    api_url = 'https://data.sfgov.org/resource/wr8u-xric.json'
    response = requests.get(api_url)
    data = response.json()

    # Connect to the PostgreSQL database
    conn = connect_to_postgre()
    cursor = conn.cursor()

    # Iterate through the data and insert into the PostgreSQL table
    for record in data:
        # Perform any necessary transformations here
        # For example, converting date strings to timestamps

        # Insert data into the PostgreSQL table

        cursor.execute(
            insert_sql,
            record['incident_number'],
            record['exposure_number'],
            record['id'],
            record['address'],
            record['incident_date'],
            record['call_number'],
            record['alarm_dttm'],
            record['arrival_dttm'],
            record['close_dttm'],
            record['city'],
            record['zipcode'],
            record['battalion'],
            record['station_area'],
            record['box'],
            record['suppression_units'],
            record['suppression_personnel'],
            record['ems_units'],
            record['ems_personnel'],
            record['other_units'],
            record['other_personnel'],
            record['first_unit_on_scene'],
            record['estimated_property_loss'],
            record['estimated_contents_loss'],
            record['fire_fatalities'],
            record['fire_injuries'],
            record['civilian_fatalities'],
            record['civilian_injuries'],
            record['number_of_alarms'],
            record['primary_situation'],
            record['mutual_aid'],
            record['action_taken_primary'],
            record['action_taken_secondary'],
            record['action_taken_other'],
            record['detector_alerted_occupants'],
            record['property_use'],
            record['area_of_fire_origin'],
            record['ignition_cause'],
            record['ignition_factor_primary'],
            record['ignition_factor_secondary'],
            record['heat_source'],
            record['item_first_ignited'],
            record['human_factors_associated_with_ignition'],
            record['structure_type'],
            record['structure_status'],
            record['floor_of_fire_origin'],
            record['fire_spread'],
            record['no_flame_spead'],
            record['number_of_floors_with_minimum_damage'],
            record['number_of_floors_with_significant_damage'],
            record['number_of_floors_with_heavy_damage'],
            record['number_of_floors_with_extreme_damage'],
            record['detectors_present'],
            record['detector_type'],
            record['detector_operation'],
            record['detector_effectiveness'],
            record['detector_failure_reason'],
            record['automatic_extinguishing_system_present'],
            record['automatic_extinguishing_sytem_type'],
            record['automatic_extinguishing_sytem_perfomance'],
            record['automatic_extinguishing_sytem_failure_reason'],
            record['number_of_sprinkler_heads_operating'],
            record['supervisor_district'],
            record['neighborhood_district'],
            record['point']
        )

    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    ingest_incidents_data()