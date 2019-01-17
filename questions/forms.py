from django import forms
from django.forms import ModelForm
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet

from questions.models import Question

class QuestionForm(ModelForm):

    class Meta:

        model = Question
        fields = ('question', )

class QuestionCompleteForm(forms.Form):

    CHOICES = {
        'NÃO',
        'SIM'
    }

    answer = forms.ChoiceField(choices=CHOICES)

class BaseQuestionSet(BaseFormSet):

    def clean(self):

        answer_list = []

        for form in self.forms:
            if form.cleaned_data:
                answer = form.cleaned_data['answer']
                answer_list.append(answer)

QuestionFormSet = formset_factory(QuestionCompleteForm, extra=1)