from celery import shared_task
import pandas as pd
import json 

DATA_CSV_FILE = 'static/data/uszips.csv'

# NOT A CELERY TASK
def read_csv_zipcodes():
    """
    Get all zip codes from csv file
    """
    print("Getting all zip codes from csv file")
    try:
        data      = pd.read_csv(DATA_CSV_FILE,
                                converters={'county_weights': eval},
                                usecols= ['zip'])
        json_data = json.loads(data.to_json())
        return True,200,json_data
    except Exception as e:
        print(e)
        return False,500,None

# NOT A CELERY TASK
def read_csv_get_document(zipCode):
    print(f"reading csv with zip_code: {zipCode}")
    try:
        data      = pd.read_csv( DATA_CSV_FILE,
                                 converters={'county_weights': eval}
                               ).query(f'zip == {zipCode}')
        json_data = json.loads(data.to_json(orient='records'))[0]
        return True,200,json_data
    except IndexError:
        json_data = {
            "error" : f"No records with zip_code {zipCode} found"
        }
        return False,404,json_data
    except Exception as e:
        print(e)
        return False,500,None

@shared_task
def update_population(zipCode,population):
    print(f"reading csv with zip_code: {zipCode}")
    try:
        # read
        data = pd.read_csv( DATA_CSV_FILE,converters={'county_weights': eval})

        # find and modify dataframe
        data.loc[data['zip'] == zipCode, 'population'] = population
        
        # save file back
        data.to_csv(DATA_CSV_FILE)
    
    except Exception as e:
        print(e)


