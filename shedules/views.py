from jsons.utils import shedules_json

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from meetings.models import Meeting
from shedules.models import Shedule
from shedules.forms import SheduleForm

@login_required
def new_shedule(request,pk):

    shedule_form = SheduleForm(request.POST or None)
    meeting = get_object_or_404(Meeting, pk=pk)
    list_topics = meeting.topics_meeting.all()

    if shedule_form.is_valid():

        shedule = shedule_form.save()
        meeting.shedule_set.add(shedule)
        shedules_json(pk)

        messages.success(request, 'Pauta Adicionada Com Sucesso!')
        return redirect('meeting_show', pk=meeting.id)

    shedule_form = SheduleForm()

    return render(request, 'shedules/new_shedule.html', {'form': shedule_form,
                                                         'list_topics': list_topics,
                                                         'meeting': meeting})

@login_required
def edit_shedule(request,pk_meeting,pk_shedule):

    shedule = Shedule.objects.get(id=pk_shedule)
    meeting = Meeting.objects.get(id=pk_meeting)
    list_topics = meeting.topics_meeting.all()

    shedule_form = SheduleForm(request.POST or None, instance=shedule)

    if shedule_form.is_valid():

        shedule_form.save()
        shedules_json(pk_meeting)

        messages.success(request, 'As Informações da Pauta Foram Alteradas Com Sucesso!')
        return redirect('meeting_show', pk = meeting.id)

    return render(request, 'shedules/edit_shedule.html', {'shedule': shedule,
                                                          'meeting': meeting,
                                                          'list_topics': list_topics})

@login_required
def show_shedule(request,pk_meeting,pk_shedule):

    shedule = get_object_or_404(Shedule,pk=pk_shedule)
    meeting = Meeting.objects.get(pk=pk_meeting)
    list_topics = meeting.topics_meeting.all()

    return render(request, 'shedules/show_shedule.html', {'shedule': shedule,
                                                          'meeting': meeting,
                                                          'list_topics': list_topics})

@login_required
def delete_shedule(request,pk_meeting,pk_shedule):

    shedule = Shedule.objects.get(id=pk_shedule)
    meeting = Meeting.objects.get(id=pk_meeting)

    if request.method == 'POST':

        shedule.delete()
        shedules_json(pk_meeting)

        messages.success(request, 'Pauta Excluída Com Sucesso!')
        return redirect('meeting_show', pk = meeting.id)

    return render(request, 'shedules/delete_shedule.html', {'shedule': shedule})