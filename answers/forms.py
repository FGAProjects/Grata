from django.forms import ModelForm

from answers.models import Answer

class AnswerForm(ModelForm):

    class Meta:

        model = Answer
        fields = ('answer_for_question', )