from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def new_topic(request,pk):

    return render(request,'topics/new_topic.html')

