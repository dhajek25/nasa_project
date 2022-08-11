from http.client import HTTPResponse
from unittest import result
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

import requests
from urllib.request import urlretrieve
import pandas as pd
import numpy as np

# Create your views here.

def home(request):
    """Function that prints the record on the home page"""
    return render(request, 'home.html', {'name':'Enter a date for your search in format YYYY-MM-DD'})

date_1 = ""
date_2 = ""

def take_date(request):
    """Function that takes input from the user and prints the input as output on the result page"""
    date_1 = request.POST['date_1']
    date_2 = request.POST['date_2']

    return render(request, date_1, date_2)

date_1 = '2022-08-08'
date_2 = '2022-08-11'

def nasa_neows():
    """The function that connects to the Nasa NeoWs API and returns data for the selected period"""
    api_key = 'cevb1Xr36zg0XJAK1is9cLIxK5cq9lW4dUw6eZcf'
    URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        'api_key':api_key,
        'start_date':date_1,
        'end_date':date_2
    }
    response = requests.get(URL_NeoFeed,params=params).json()
    return response

object_data = nasa_neows()

def data_extraction():
    """The function that processes the response data from the API and extracts the required information from the dictionary"""
    data_values = pd.DataFrame()
    for key, values in object_data["near_earth_objects"].items():
        for i in values:
            name = {key: i["name"]} 
            diameter = {key: i["estimated_diameter"]["kilometers"]["estimated_diameter_max"]}
            date_full = {key: i["close_approach_data"][0]["close_approach_date_full"]}
            miss_distance = {key: i["close_approach_data"][0]["miss_distance"]["astronomical"]}
            empty_df = pd.DataFrame()
            empty_df["name"] = (list(name.values()))
            empty_df["diameter"] = list(diameter.values())
            empty_df["date_full"] = list(date_full.values())
            empty_df["miss_distance"] = list(miss_distance.values())
            data_values = data_values.append(empty_df)
    return data_values

data_values = data_extraction()

# Convert data to desired format

data_values["date_full"] = pd.to_datetime(data_values["date_full"])

data_values["miss_distance"] = pd.to_numeric(data_values["miss_distance"])

data_values.sort_values(by=["miss_distance"], inplace=True)

data_values.index = np.arange(1, len(data_values) + 1)

data_values = data_values.head().to_html()

def take_date(request):
    """Function that prints the record on the result page as a table"""
    return render(request, 'result.html', {'final_table':data_values})


