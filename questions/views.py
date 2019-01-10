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

@login_required
def edit_question(request,pk_question,pk_meeting,pk_quiz):

    question = get_object_or_404(Question, pk=pk_question)
    question_form = QuestionForm(request.POST or None,instance=question)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)
    quiz = get_object_or_404(Quiz, pk=pk_quiz)

    if question_form.is_valid():

        question_form.save()

        messages.success(request, 'Informações da Pergunta Alterada Com Sucesso!')
        return redirect('/ver_questionario/' + str(meeting.id) + '/' + str(quiz.id))

    return render(request, 'questions/edit_question.html', {'question': question,
                                                            'meeting' : meeting,
                                                            'quiz': quiz})

@login_required
def delete_question(request,pk_question,pk_meeting,pk_quiz):

    question = get_object_or_404(Question, pk=pk_question)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)
    quiz = get_object_or_404(Quiz, pk=pk_quiz)

    if request.method == 'POST':

        question.delete()
        messages.success(request, 'Pergunta Excluída Com Sucesso!')
        return redirect('/ver_questionario/' + str(meeting.id) + '/' + str(quiz.id))

    return render(request, 'questions/delete_question.html', {'question': question,
                                                            'meeting': meeting,
                                                            'quiz': quiz})