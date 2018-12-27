from django.forms import ModelForm
from topics.models import Topic

class TopicForm(ModelForm):

    class Meta:

        model = Topic
        fields = ('topic_name',)