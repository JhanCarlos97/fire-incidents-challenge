import requests
from datetime import datetime
from utils.connect_to_db import connect_to_postgre

def ingest_incidents_data():

    # Read the SQL statement from the file
    with open('sql/insert_raw_incidents_data.sql', 'r') as sql_file:
        insert_sql = sql_file.read()

    print('Fectching data from API')

    # Fetch data from the API endpoint
    api_url = 'https://data.sfgov.org/resource/wr8u-xric.json'
    response = requests.get(api_url, params={'$limit': 1000000})
    data = response.json()

    # Connect to the PostgreSQL database
    conn = connect_to_postgre()
    cursor = conn.cursor()

    print('Connected to local db')

    # Get the maximum incident_date from the database
    cursor.execute("SELECT MAX(incident_date) FROM test.raw_incidents")
    max_incident_date = cursor.fetchone()[0]

    # If no records in the table, set max_incident_date to a past date
    if max_incident_date is None:
        max_incident_date = datetime(1900, 1, 1)
    else:
        max_incident_date = datetime.strptime(str(max_incident_date), '%Y-%m-%d %H:%M:%S')

    # Filter data based on incident_date
    recent_data = [record for record in data if datetime.strptime(record['incident_date'], '%Y-%m-%dT%H:%M:%S') > max_incident_date]

    if len(recent_data) == 0:
        print('No new data')
    else:    
        print('Adding '+str(len(recent_data))+' new incidents')
        print('Loading data')

        # Iterate through the data and insert into the PostgreSQL table
        for record in recent_data:

            # Insert data into the PostgreSQL table

            cursor.execute(
                insert_sql,
                (
                    record.get('incident_number', None),
                    record.get('exposure_number', None),
                    record['id'],
                    record.get('address', None),
                    record.get('incident_date', None),
                    record.get('call_number', None),
                    record.get('alarm_dttm', None),
                    record.get('arrival_dttm', None),
                    record.get('close_dttm', None),
                    record.get('city', None),
                    record.get('zipcode', None),
                    record.get('battalion', None),
                    record.get('station_area', None),
                    record.get('box', None),
                    record.get('suppression_units', None),
                    record.get('suppression_personnel', None),
                    record.get('ems_units', None),
                    record.get('ems_personnel', None),
                    record.get('other_units', None),
                    record.get('other_personnel', None),
                    record.get('first_unit_on_scene', None),
                    record.get('estimated_property_loss', None),
                    record.get('estimated_contents_loss', None),
                    record.get('fire_fatalities', None),
                    record.get('fire_injuries', None),
                    record.get('civilian_fatalities', None),
                    record.get('civilian_injuries', None),
                    record.get('number_of_alarms', None),
                    record.get('primary_situation', None),
                    record.get('mutual_aid', None),
                    record.get('action_taken_primary', None),
                    record.get('action_taken_secondary', None),
                    record.get('action_taken_other', None),
                    record.get('detector_alerted_occupants', None),
                    record.get('property_use', None),
                    record.get('area_of_fire_origin', None),
                    record.get('ignition_cause', None),
                    record.get('ignition_factor_primary', None),
                    record.get('ignition_factor_secondary', None),
                    record.get('heat_source', None),
                    record.get('item_first_ignited', None),
                    record.get('human_factors_associated_with_ignition', None),
                    record.get('structure_type', None),
                    record.get('structure_status', None),
                    record.get('floor_of_fire_origin', None),
                    record.get('fire_spread', None),
                    record.get('no_flame_spead', None),
                    record.get('number_of_floors_with_minimum_damage', None),
                    record.get('number_of_floors_with_significant_damage', None),
                    record.get('number_of_floors_with_heavy_damage', None),
                    record.get('number_of_floors_with_extreme_damage', None),
                    record.get('detectors_present', None),
                    record.get('detector_type', None),
                    record.get('detector_operation', None),
                    record.get('detector_effectiveness', None),
                    record.get('detector_failure_reason', None),
                    record.get('automatic_extinguishing_system_present', None),
                    record.get('automatic_extinguishing_sytem_type', None),
                    record.get('automatic_extinguishing_sytem_perfomance', None),
                    record.get('automatic_extinguishing_sytem_failure_reason', None),
                    record.get('number_of_sprinkler_heads_operating', None),
                    record.get('supervisor_district', None),
                    record.get('neighborhood_district', None),
                    str(record['point'].get('coordinates')) if 'point' in record and 'coordinates' in record['point'] else None
                )
            )
        
        print('Data loaded')

    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    ingest_incidents_data()