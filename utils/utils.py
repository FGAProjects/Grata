import json

from shedules.models import Shedule
from topics.models import Topic
from questions.models import Question

def list_shedules():

    shedules = open('jsons/shedule.json', 'r')
    read_shedules = json.load(shedules)
    shedules.close()
    list_shedules = read_shedules
    shedule = Shedule()
    shedules_list = []

    for aux in range(len(list_shedules)):

        shedule.introduction = \
            list_shedules[aux].get('Shedules').get('introduction')

        shedule.review_of_the_management_perspective = \
            list_shedules[aux].get('Shedules').get('review_of_the_management_perspective')

        shedule.vision_of_the_area_of_informativa = \
            list_shedules[aux].get('Shedules').get('vision_of_the_area_of_informativa')

        shedule.rules_of_conduct = \
            list_shedules[aux].get('Shedules').get('rules_of_conduct')

        shedules_list.append(Shedule('',
                                     shedule.introduction,
                                     shedule.review_of_the_management_perspective,
                                     shedule.vision_of_the_area_of_informativa,
                                     shedule.rules_of_conduct))

    return shedules_list

def list_topics():

    topics = open('jsons/topic.json', 'r')
    read_topics = json.load(topics)
    topics.close()
    list_topics = read_topics
    topic = Topic()
    topics_list = []

    for aux in range(len(list_topics)):

        topic.topic_name = \
            list_topics[aux].get('Topics').get('topic_name')

        topics_list.append(Topic('',
                                     topic.topic_name))

    return topics_list

def list_questions():

    questions = open('jsons/question.json', 'r')
    read_questions = json.load(questions)
    questions.close()
    list_questions = read_questions
    question = Question()
    questions_list = []

    for aux in range(len(list_questions)):

        question.question = \
            list_questions[aux].get('Questions').get('question')
        question.answer = list_questions[aux].get('Questions').get('answer')

        questions_list.append(Question('',
                                            question.question,
                                            question.answer))

    return questions_list