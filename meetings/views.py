from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from meetings.models import Meeting
from meetings.forms import MeetingForm

# class MeetingView(DetailView):
#     model = Meeting
#     template_name = 'meetings/detail_meeting.html'
#
# class MeetingUpdate(UpdateView):
#     model = Meeting
#     fields = ['subject_matter', 'project', 'meeting_leader', 'documentary', 'first_date',
#               'final_date', 'first_hour', 'final_hour']
#     success_url = reverse_lazy('meeting_list')
#
# class MeetingDelete(DeleteView):
#     model = Meeting
#     success_url = reverse_lazy('meeting_list')

# class NewMeeting(CreateView):
#
#     model = Meeting
#     template_name = 'meetings/new_meeting.html'
#     fields = ['subject_matter', 'project', 'meeting_leader', 'documentary', 'first_date',
#               'final_date', 'first_hour', 'final_hour']
#     success_url = reverse_lazy('meeting_list')

# @login_required
# def meeting_show(request):
#
#     return render(request,'meetings/show_meeting.html')
#
# @login_required
# def meeting_list(request):
#
#     return render(request,'meetings/list_meeting.html')

# @login_required
# def meeting_lists(request):
#
#     meeting = Meeting.objects.all()
#     data = {}
#     data['meeting_list'] = meeting
#
#     return render(request,'meetings/lists_meeting.html',data)


@login_required
def new_meeting(request):

    meeting = MeetingForm(request.POST or None)

    if meeting.is_valid():

        meeting.save()
        return redirect('meeting_list')

    return render(request, 'meetings/new_meeting.html', {'meeting': meeting})

@login_required
def list_meeting(request):

    meeting = Meeting.objects.all()

    return render(request, 'meetings/list_meeting.html',{'list_meeting':meeting})

@login_required
def show_meeting(request,pk):

    meeting = get_object_or_404(Meeting,pk=pk)

    return render(request, 'meetings/show_meeting.html',{'meeting':meeting})

@login_required
def edit_meeting(request,pk):

    meeting = get_object_or_404(Meeting, pk=pk)
    meetings = MeetingForm(request.POST or None, instance=meeting)

    if meetings.is_valid():

        meetings.save()
        return redirect('meeting_list')

    return render(request, 'meetings/edit_meeting.html', {'meeting': meetings})