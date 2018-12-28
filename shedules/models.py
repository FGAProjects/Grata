from django.db import models

from meetings.models import Meeting

class Shedule(models.Model):

    introduction = models.CharField(max_length=400)
    review_of_the_management_perspective = models.CharField(max_length=150)
    vision_of_the_area_of_informativa = models.CharField(max_length=200)
    rules_of_conduct = models.CharField(max_length=400)

    shedule_meeting = models.ForeignKey(Meeting, null=True, blank=True, on_delete=models.CASCADE)