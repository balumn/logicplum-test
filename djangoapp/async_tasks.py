from celery import shared_task
import pandas as pd
import json 

DATA_CSV_FILE = 'static/data/uszips.csv'

# NOT A CELERY TASK
def read_csv_zipcodes():
    """
    Get all zip codes from csv file
    """
    print("reading csv with pandas")
    try:
        data      = pd.read_csv(DATA_CSV_FILE,
                                converters={'county_weights': eval},
                                usecols= ['zip'])
        json_data = json.loads(data.to_json())
        status    = True
    except Exception as e:
        print(e)
        json_data = None
        status    = False
    return status,json_data

def read_csv_get_document(zipCode):
    print(f"reading csv with zip_code: {zipCode}")
    try:
        data        = pd.read_csv( DATA_CSV_FILE,
                            converters={'county_weights': eval}
                        ).query(f'zip == {zipCode}')
        json_data   = json.loads(data.to_json(orient='records'))[0]
        status      = True
        status_code = 200
    except IndexError:
        json_data   = {
            "error" : f"No records with zip_code {zipCode} found"
        }
        status      = False
        status_code = 404
    except Exception as e:
        print(e)
        json_data   = None
        status      = False
        status_code = 500
    return status,status_code,json_data