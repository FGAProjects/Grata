from jsons.utils import topics_json

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from topics.models import Topic
from topics.forms import TopicForm
from meetings.models import Meeting

@login_required
def new_topic(request,pk):

    topic_form = TopicForm(request.POST or None)
    meeting = get_object_or_404(Meeting, pk=pk)
    list_topics = meeting.topics_meeting.all()

    if topic_form.is_valid():

        topic = topic_form.save()
        meeting.topics_meeting.add(topic)
        topics_json(pk)

        messages.success(request, 'Tópico Adicionado Com Sucesso!')
        return redirect('topic_new', pk=meeting.id)

    topic_form = TopicForm()

    return render(request, 'topics/new_topic.html', {'form': topic_form,
                                                     'list_topics': list_topics,
                                                     'meeting': meeting})

@login_required
def delete_topic(request,pk,pk_meeting):

    topic = Topic.objects.get(id=pk)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)

    if request.method == 'POST':

        topic.delete()
        topics_json(pk_meeting)

        messages.success(request, 'Tópico Excluído Com Sucesso!')
        return redirect('topic_new', pk=meeting.id)

    return render(request, 'topics/delete_topic.html', {'topic': topic,
                                                        'meeting':meeting})