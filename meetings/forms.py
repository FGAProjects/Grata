from django.forms import ModelForm

from meetings.models import Meeting

class MeetingForm(ModelForm):

    class Meta:

        model = Meeting
        fields = ['subject_matter', 'project', 'meeting_leader', 'local', 'documentary', 'first_date',
                  'final_date', 'first_hour', 'final_hour']

class EditMeetingForm(ModelForm):

    class Meta:

        model = Meeting
        fields = ['subject_matter', 'project', 'meeting_leader', 'local', 'documentary', 'first_date',
                  'final_date', 'first_hour', 'final_hour', 'status']