import json

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers

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
        shedule_list = meeting.shedule_set.all()

        shedule_data = []

        for shedule in shedule_list:

            with open('jsons/shedule.json', 'w') as write_file:

                shedule_list = {

                    'Shedule_' + str(shedule.id): {
                        'introduction': shedule.introduction,
                        'review_of_the_management_perspective': shedule.review_of_the_management_perspective,
                        'vision_of_the_area_of_informativa': shedule.vision_of_the_area_of_informativa,
                        'rules_of_conduct': shedule.rules_of_conduct
                    }
                }

                shedule_data.append(shedule_list)
                json.dump(shedule_data, write_file)

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
    shedule_data = []

    shedule_form = SheduleForm(request.POST or None, instance=shedule)

    if shedule_form.is_valid():

        shedule_form.save()
        shedule_list = meeting.shedule_set.all()

        for shedule in shedule_list:

            with open('jsons/shedule.json', 'w') as write_file:

                shedule_list = {

                    'Shedule_' + str(shedule.id): {
                        'introduction': shedule.introduction,
                        'review_of_the_management_perspective': shedule.review_of_the_management_perspective,
                        'vision_of_the_area_of_informativa': shedule.vision_of_the_area_of_informativa,
                        'rules_of_conduct': shedule.rules_of_conduct
                    }
                }

                shedule_data.append(shedule_list)
                json.dump(shedule_data, write_file)

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
        shedule_list = meeting.shedule_set.all()
        shedule_data = []

        for shedule in shedule_list:

            with open('jsons/shedule.json', 'w') as write_file:

                shedule_list = {

                    'Shedule_' + str(shedule.id): {
                        'introduction': shedule.introduction,
                        'review_of_the_management_perspective': shedule.review_of_the_management_perspective,
                        'vision_of_the_area_of_informativa': shedule.vision_of_the_area_of_informativa,
                        'rules_of_conduct': shedule.rules_of_conduct
                    }
                }

                shedule_data.append(shedule_list)
                json.dump(shedule_data, write_file)

        messages.success(request, 'Pauta Excluída Com Sucesso!')
        return redirect('meeting_show', pk = meeting.id)

    return render(request, 'shedules/delete_shedule.html', {'shedule': shedule})