from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from meetings.models import Meeting
from questionnaires.models import Quiz
from questions.models import Question
from questions.forms import QuestionForm

@login_required
def show_question(request,pk_meeting,pk_quiz):

    question_form = QuestionForm(request.POST or None)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)
    quiz = get_object_or_404(Quiz, pk=pk_quiz)
    list_questions = quiz.question_questionnaires.all()
    all_questions = Question.objects.all()

    if question_form.is_valid():

        question = question_form.save()
        quiz.question_questionnaires.add(question)

        messages.success(request, 'Pergunta Adicionada Com Sucesso!')
        return redirect('/ver_questionario/'+ str(meeting.id) + '/' + str(quiz.id))

    quiz_form = QuestionForm()

    return render(request, 'questions/show_quiz.html', {'form': quiz_form,
                                                        'meeting': meeting,
                                                        'list_questions': list_questions,
                                                        'quiz': quiz,
                                                        'all_questions': all_questions})

"""
@login_required
def edit_quiz(request, pk_meeting, pk_quiz):
    quiz = Quiz.objects.get(id=pk_quiz)
    quiz_form = QuestionnairesForm(request.POST or None, instance=quiz)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)

    if quiz_form.is_valid():
        quiz_form.save()

        messages.success(request, 'Informações da Pergunta Alterada Com Sucesso!')
        return redirect('quiz_new', pk=meeting.id)

    return render(request, 'questionnaires/edit_question.html', {'quiz': quiz,
                                                             'meeting': meeting})


@login_required
def delete_quiz(request, pk_meeting, pk_quiz):
    quiz = Quiz.objects.get(id=pk_quiz)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)

    if request.method == 'POST':
        quiz.delete()

        messages.success(request, 'Pergunta Excluída Com Sucesso!')
        return redirect('quiz_new', pk=meeting.id)

    return render(request, 'questionnaires/delete_question.html', {'quiz': quiz,
                                                               'meeting': meeting})
"""
