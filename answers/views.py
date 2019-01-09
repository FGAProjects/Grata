from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from meetings.models import Meeting

@login_required
def list_quiz(request,pk):

    meeting = get_object_or_404(Meeting, pk=pk)
    list_questions = meeting.questionnaires_meeting.all()
    list_option = {

        'NÃO',
        'SIM',
    }

    return render(request, 'questionnaires/list_questions.html', {'questions': list_questions,
                                                                  'options': list_option,
                                                                  'meeting': meeting})