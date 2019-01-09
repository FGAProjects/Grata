from django import forms
from django.forms import ModelForm

from questionnaires.models import Quiz

class QuestionnairesForm(ModelForm):

    class Meta:

        model = Quiz
        description = forms.CharField(max_length=10)

        fields = ('description', )