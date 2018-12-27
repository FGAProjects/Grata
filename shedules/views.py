from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from meetings.models import Meeting
from shedules.forms import SheduleForm

@login_required
def new_shedule(request,pk):

    shedule_form = SheduleForm(request.POST or None)

    meeting = get_object_or_404(Meeting, pk=pk)

    list_topics = meeting.topics_meeting.all()

    if shedule_form.is_valid():

        shedule = shedule_form.save()

        # meeting.shedules_meeting.add(shedule)
        messages.success(request, 'Pauta Adicionada Com Sucesso!')
        return redirect('meeting_show', pk=meeting.id)

    shedule_form = SheduleForm()

    return render(request, 'shedules/new_shedule.html', {'form': shedule_form, 'list_topics': list_topics,
                                                     'meeting': meeting})