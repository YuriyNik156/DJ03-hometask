from generalnews.shortcuts import render
from generalnews.http import HttpResponse

def index(request):
    data = {
        'caption':'ZeroDjango'
    }
    return render(request, "main/index.html", data)

def new(request):
    return render(request, "main/new.html")



