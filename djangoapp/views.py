from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .async_tasks import *
import json
from rest_framework.parsers import JSONParser
from django.http import QueryDict
from django.shortcuts import render

@api_view(['GET'])
def api_zip_codes(request):
    _status,status_code,data = read_csv_zipcodes() # NOT AN ASYNC TASK
    
    save_api(request.path,request.method,_status,status_code) # save api details
    return JsonResponse(
        {
            "status": _status,
            "zip"   : data
        },status = status_code
    )

@api_view(['GET'])
def api_get_data_from_zip(request, zipCode):
    print(zipCode)

    _status,status_code,data = read_csv_get_document(zipCode) # NOT AN ASYNC TASK
    save_api(request.path,request.method,_status,status_code) # save api details
    return JsonResponse(
        {
            "status"    : _status,
            "document"  : data
        },status = status_code
    )

@api_view(['PUT','POST'])
def api_modify_data(request):
    if request.method == "PUT":
        # update row with population where `zip`== zip
        try:
            data_input = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            save_api(request.path,request.method,False,400) # save api details
            return JsonResponse({"status":False,"error":f"{e}: Json Parsing error"},status = 400)
        try:
            _zip = data_input["zip"]
            population = data_input["population"]
        except KeyError as e:
            save_api(request.path,request.method,False,400) # save api details
            return JsonResponse({"status":False,"error":f"{e} is a must parameter"},status = 400)
        
        _status,status_code,data = read_csv_get_document(_zip) # checking if row exists
        if status_code == 404:
            save_api(request.path,request.method,False,404) # save api details
            return JsonResponse({"status":False,"error":"No such zip code found"},status = 404)

        update_population.delay(_zip,population) # celery task
        save_api(request.path,request.method,True,200) # save api details
        return JsonResponse(
            {
                "status" : True,
                "job"    : "Initialized"
            },status = 200
        )
    elif request.method == "POST":
        # add a new row onto CSV
        try:
            data_input = json.loads(request.body)
        except Exception as e:
            save_api(request.path,request.method,False,400) # save api details
            return JsonResponse({"status":False,"error":f"{e}: Json Parsing error"},status = 400)
        try:
            _zip             = int(data_input["zip"])
            population       = int(data_input["population"])
            lat              = float(data_input["lat"])
            lng              = float(data_input["lng"])
            city             = data_input["city"]
            state_id         = data_input["state_id"]
            state_name       = data_input["state_name"]
            zcta             = data_input["zcta"]
            parent_zcta      = data_input["parent_zcta"]
            density          = float(data_input["density"])
            county_fips      = int(data_input["county_fips"])
            county_name      = data_input["county_name"]
            county_weights   = data_input["county_weights"]
            county_names_all = data_input["county_names_all"]
            county_fips_all  = data_input["county_fips_all"]
            imprecise        = data_input["imprecise"]
            military         = data_input["military"]
            timezone         = data_input["timezone"]
        except KeyError as e:
            save_api(request.path,request.method,False,400) # save api details
            return JsonResponse({"status":False,"error":f"{e} is a must parameter"},status = 400)
        except ValueError as e:
            save_api(request.path,request.method,False,400) # save api details
            return JsonResponse({"status":False,"error":f"{e}"},status = 400)
        
        # parameter validations checking
        if not(
                (type(zcta)             == bool) and \
                (type(imprecise)        == bool) and \
                (type(military)         == bool) and \
                (type(city)             == str) and \
                (type(state_id)         == str) and \
                (type(state_name)       == str) and \
                (type(county_name)      == str) and \
                (type(county_names_all) == str) and \
                (type(county_fips_all)  == str)
            ):
                # True case of this if => any of the parameter is not of required type
                save_api(request.path,request.method,False,400) # save api details
                return JsonResponse({"status":False,"error":f"Parameter validations checking failed"},status = 400)
            
        _status,status_code,data = read_csv_get_document(_zip) # checking if row exists
        if status_code == 200:
            save_api(request.path,request.method,False,400) # save api details
            return JsonResponse({"status":False,"error":"Given zip code already found"},status = 400)
        
        # celery task
        insert_row.delay(
            _zip,
            lat,
            lng,
            city,
            state_id,
            state_name,
            zcta,
            parent_zcta,
            population,
            density,
            county_fips,
            county_name,
            county_weights,
            county_names_all,
            county_fips_all,
            imprecise,
            military,
            timezone  
        )
        save_api(request.path,request.method,True,200) # save api details
        return JsonResponse(
            {
                "status" : True,
                "job"    : "Initialized"
            },status = 200
        )


def index(request):
    """
    A simple view for displaying Home_page.
    My homepage is my Readme file itself.
    PS: this HTML is auto-generated from "https://markdowntohtml.com/"
    """
    return render(request, 'index.html')
