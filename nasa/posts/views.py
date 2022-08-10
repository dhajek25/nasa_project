from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm


# Create your views here.

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form })

def take(request):
    if request.method == "POST":
        date1 = request.GET["date1"]
        date2 = request.GET["date2"]
        res = date1 + date2
    return render(request, "posts/result.html", {"result": res})
