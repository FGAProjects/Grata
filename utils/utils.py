import json
from django.shortcuts import get_object_or_404

from meetings.models import Meeting

def meetings_json():

    meeting_list = Meeting.objects.all()
    meeting_data = []

    for meeting_datas in meeting_list:

        with open('jsons/meeting.json', 'w') as write_file:

            meeting_list = {

                'Meeting_' + str(meeting_datas.id): {
                    'subject_matter': meeting_datas.subject_matter,
                    'project': meeting_datas.project,
                    'local': meeting_datas.local,
                    'meeting_leader': meeting_datas.meeting_leader,
                    'documentary': meeting_datas.documentary,
                    'first_date': meeting_datas.first_date,
                    'final_date': meeting_datas.final_date,
                    'first_hour': meeting_datas.first_hour,
                    'final_hour': meeting_datas.final_hour
                }
            }

            meeting_data.append(meeting_list)
            json.dump(meeting_data, write_file)

def shedules_json(pk):

    meeting = get_object_or_404(Meeting, pk=pk)
    shedule_list = meeting.shedule_set.all()

    shedule_data = []

    for shedule in shedule_list:

        with open('jsons/shedule.json', 'w') as write_file:

            shedule_list = {

                'Shedule_' + str(shedule.id): {
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

                'Topic_' + str(topic.id): {

                    'topic_name': topic.topic_name
                }
            }

            topic_data.append(topic_list)

            json.dump(topic_data, write_file)