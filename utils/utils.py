import json

from shedules.models import Shedule
from topics.models import Topic

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

