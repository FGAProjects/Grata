from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, "base.html",{})

def about(request):

    context = {

    }
    return render(request, "about.html", context)

def contact(request):

    context = {

    }
    return render(request, "contact.html",context)