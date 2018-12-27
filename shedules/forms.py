from django.forms import ModelForm
from shedules.models import Shedule

class SheduleForm(ModelForm):

    class Meta:

        model = Shedule
        fields = ['introduction', 'review_of_the_management_perspective',
                  'vision_of_the_area_of_informativa', 'rules_of_conduct']