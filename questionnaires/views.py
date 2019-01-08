from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from meetings.models import Meeting
from questionnaires.models import Quiz
from questionnaires.forms import QuestionnairesForm

@login_required
def new_quiz(request,pk):

    quiz_form = QuestionnairesForm(request.POST or None)
    meeting = get_object_or_404(Meeting, pk=pk)
    list_questions = meeting.questionnaires_meeting.all()

    if quiz_form.is_valid():

        quiz = quiz_form.save()
        meeting.questionnaires_meeting.add(quiz)

        messages.success(request, 'Pergunta Adicionada Com Sucesso!')
        return redirect('quiz_new', pk=meeting.id)

    quiz_form = QuestionnairesForm()

    return render(request, 'questionnaires/new_quiz.html', {'form': quiz_form,
                                                            'meeting': meeting,
                                                            'questions': list_questions})

@login_required
def edit_quiz(request,pk_meeting,pk_quiz):

    quiz = Quiz.objects.get(id=pk_quiz)
    quiz_form = QuestionnairesForm(request.POST or None,instance=quiz)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)

    if quiz_form.is_valid():

        quiz_form.save()

        messages.success(request, 'Informações da Pergunta Alterada Com Sucesso!')
        return redirect('quiz_new', pk=meeting.id)

    return render(request, 'questionnaires/edit_quiz.html', {'quiz': quiz,
                                                            'meeting': meeting})

@login_required
def delete_quiz(request,pk_meeting,pk_quiz):

    quiz = Quiz.objects.get(id=pk_quiz)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)

    if request.method == 'POST':

        quiz.delete()

        messages.success(request, 'Pergunta Excluída Com Sucesso!')
        return redirect('quiz_new', pk=meeting.id)

    return render(request, 'questionnaires/delete_quiz.html', {'quiz': quiz,
                                                             'meeting': meeting})