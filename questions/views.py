from jsons.utils import questions_json

from django.shortcuts import render,redirect,get_object_or_404
from django.forms import formset_factory

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from meetings.models import Meeting
from questionnaires.models import Quiz
from questions.models import Question
from questions.forms import QuestionForm,QuestionCompleteForm

@login_required
def show_question(request,pk_meeting,pk_quiz):

    question_form = QuestionForm(request.POST or None)
    meeting = get_object_or_404(Meeting, pk=pk_meeting)
    quiz = get_object_or_404(Quiz, pk=pk_quiz)
    list_questions = quiz.question_questionnaires.all()

    if question_form.is_valid():

        question = question_form.save(commit=False)
        question.question = question_form.cleaned_data.get('question')
        question.answer = ''
        question.save()
        quiz.question_questionnaires.add(question)

        messages.success(request, 'Pergunta Adicionada Com Sucesso!')
        return redirect('/ver_questionario/'+ str(meeting.id) + '/' + str(quiz.id))

    quiz_form = QuestionForm()

    return render(request, 'questions/show_quiz.html', {'form': quiz_form,
                                                        'meeting': meeting,
                                                        'list_questions': list_questions,
                                                        'quiz': quiz})

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

@login_required
def respond_question(request,pk_meeting,pk_quiz):

    meeting = get_object_or_404(Meeting, pk=pk_meeting)
    quiz = get_object_or_404(Quiz, pk=pk_quiz)
    list_questions = quiz.question_questionnaires.all()
    BaseQuestionFormSet = formset_factory(QuestionCompleteForm,extra=len(list_questions))
    options = {
        'NÃO',
        'SIM'
    }
    cont = 1
    questions = []

    if request.method == 'POST' or request.method == 'post':

        question_form = BaseQuestionFormSet(request.POST)

        if question_form.is_valid():

            for auxQuestion in list_questions:

                questions.append(auxQuestion)

            for aux in range(len(list_questions)):

                question = Question()

                question_id = request.POST.get('question_' + str(cont))
                answer = request.POST.get('answer_' + str(question_id))
                question_remove = Question.objects.get(id=questions[aux].id)
                cont +=1

                question.question = questions[aux].question
                question.answer = answer

                if answer != None:

                    quiz.question_questionnaires.remove(question_remove)
                    question_remove.delete()

                    question.save()
                    quiz.question_questionnaires.add(question)
                    questions_json(pk_quiz)

            messages.success(request, 'Questionário Respondido Com Sucesso!')
            return redirect('meeting_show', pk=meeting.id)

    else:

        question_form = BaseQuestionFormSet()

    return render(request, 'questions/respond_question.html', {'formset': question_form,
                                                               'meeting': meeting,
                                                               'quiz': quiz,
                                                               'list_questions': list_questions,
                                                               'options' : options})

def question_list(request, pk_meeting, pk_quiz):

    meeting = get_object_or_404(Meeting, pk=pk_meeting)
    quiz = get_object_or_404(Quiz, pk=pk_quiz)
    list_questions = Question.objects.filter(quiz__id=quiz.id)

    return render(request, 'questions/question_list.html', {'meeting': meeting,
                                                            'quiz': quiz,
                                                            'list_questions': list_questions})