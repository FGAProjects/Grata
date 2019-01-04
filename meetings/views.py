from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from meetings.models import Meeting
from meetings.forms import MeetingForm,EditMeetingForm

@login_required
def new_meeting(request):

    meeting = MeetingForm(request.POST or None)

    if meeting.is_valid():

        meeting.save()

        messages.success(request,'Reunião Criada Com Sucesso!')
        return redirect('meeting_list')

    return render(request, 'meetings/new_meeting.html', {'meeting': meeting})

@login_required
def list_meeting(request):

    meeting = Meeting.objects.all()

    return render(request, 'meetings/list_meeting.html',{'list_meeting':meeting})

@login_required
def show_meeting(request,pk):

    meeting = get_object_or_404(Meeting,pk=pk)
    shedules = meeting.shedule_set.all()
    list_topics = meeting.topics_meeting.all()

    return render(request, 'meetings/show_meeting.html',{'meeting':meeting,
                                                         'list_topics':list_topics,
                                                         'shedules':shedules})

@login_required
def edit_meeting(request,pk):

    meeting = Meeting.objects.get(id=pk)
    meeting_form = EditMeetingForm(request.POST or None, instance=meeting)

    if meeting_form.is_valid():

        meeting = meeting_form.save()

        messages.success(request, 'Informações da Reunião Foram Alteradas Com Sucesso!')
        return redirect('meeting_show', pk=meeting.id)

    return render(request, 'meetings/edit_meeting.html', {'meeting': meeting})

@login_required
def delete_meeting(request,pk):

    meeting = Meeting.objects.get(id=pk)

    if request.method == 'POST':

        meeting.delete()

        messages.success(request, 'Reunião Excluída Com Sucesso!')
        return redirect('meeting_list')

    return render(request, 'meetings/delete_meeting.html', {'meeting': meeting})