from celery import shared_task
import os
import pandas as pd
import json 

DATA_CSV_FILE = 'static/data/uszips.csv'

# NOT A CELERY TASK
def read_csv_zipcodes():
    print("reading csv with pandas")
    try:
        data      = pd.read_csv(DATA_CSV_FILE,converters={'county_weights': eval},usecols= ['zip'])
        json_data = json.loads(data.to_json())
        status    = True
    except Exception as e:
        print(e)
        json_data = None
        status    = False
    return status,json_data
