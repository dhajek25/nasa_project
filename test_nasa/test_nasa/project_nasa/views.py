from http.client import HTTPResponse
from unittest import result
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import pandas as pd
import numpy as np

# Create your views here.

def home(request):
    """Function that prints the record on the home page"""
    return render(request, 'home.html', {'name':'Enter a date for your search in format YYYY-MM-DD'})

def take_date(request):
    """Function that takes input from the user and prints the input as output on the result page"""
    date_1 = request.GET['date_1']
    date_2 = request.GET['date_2']

    return render(request, "result.html", {'result':[date_1, date_2]})
