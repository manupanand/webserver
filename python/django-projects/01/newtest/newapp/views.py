from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_hello(request):
    # dictionary
    movie_details={'movies':[{
        "title":"some movie",
        "year":2000,
        "summary":"some summary",
        "success":True
    },{
        "title":"some movie",
        "year":2000,
        "summary":"some summary",
        "success":True
    },{
        "title":"some movie",
        "year":2000,
        "summary":"some summary",
        "success":True
    },{
        "title":"some movie",
        "year":2000,
        "summary":"some summary",
        "success":True
    }]}
    return render(request,'index.html',movie_details)
