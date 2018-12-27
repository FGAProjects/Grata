from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory

from topics.models import Topic
from meetings.models import Meeting

@login_required
def new_topic(request,pk):

    TopicFormSet = modelformset_factory(Topic, fields=('topic_name',),extra=1)

    meeting = get_object_or_404(Meeting, pk=pk)

    list = Topic.objects.all()

    if request.method == 'POST':

        form = TopicFormSet(request.POST)
        form.save()

    form = TopicFormSet()

    return render(request,'topics/new_topic.html',{'form':form,'lists':list,'meeting':meeting})

def delete_topic(request,pk,pk_meeting):

    topic = Topic.objects.get(id=pk)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)

    if request.method == 'POST':
        topic.delete()
        messages.success(request, 'Tópico Excluída Com Sucesso')
        return redirect('new_topic', pk=meeting.id)

    return render(request, 'topics/delete_topic.html', {'topic': topic,'meeting':meeting})