from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def meeting_show(request):

    return render(request,'meetings/show_meeting.html')

@login_required
def meeting_list(request):

    return render(request,'meetings/list_meeting.html')