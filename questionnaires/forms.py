from django.forms import ModelForm

from questionnaires.models import Quiz

class QuestionnairesForm(ModelForm):

    class Meta:

        model = Quiz

        fields = ('description', )