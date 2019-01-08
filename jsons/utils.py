import json
from django.shortcuts import get_object_or_404

from meetings.models import Meeting

def shedules_json(pk):

    meeting = get_object_or_404(Meeting, pk=pk)
    shedule_list = meeting.shedule_set.all()

    shedule_data = []

    for shedule in shedule_list:

        with open('jsons/shedule.json', 'w') as write_file:

            shedule_list = {
                'Shedules' : {
                    'introduction': shedule.introduction,
                    'review_of_the_management_perspective': shedule.review_of_the_management_perspective,
                    'vision_of_the_area_of_informativa': shedule.vision_of_the_area_of_informativa,
                    'rules_of_conduct': shedule.rules_of_conduct
                }
            }

            shedule_data.append(shedule_list)
            json.dump(shedule_data, write_file)

def topics_json(pk):

    meeting = get_object_or_404(Meeting, pk=pk)
    list_topics = meeting.topics_meeting.all()

    topic_data = []

    for topic in list_topics:

        with open('jsons/topic.json', 'w') as write_file:

            topic_list = {
                'Topics' : {
                    'topic_name': topic.topic_name
                }
            }

            topic_data.append(topic_list)

            json.dump(topic_data, write_file)