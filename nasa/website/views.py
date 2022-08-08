from django.shortcuts import render
from django.http import HttpResponse

#The welcome view
def welcome(request):
    return render(request, "website/welcome.html")