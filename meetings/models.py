from django.db import models
from django.urls import reverse

from topics.models import Topic
from shedules.models import Shedule

class Meeting(models.Model):

    subject_matter = models.CharField(max_length=40)
    project = models.CharField(max_length=40)
    local = models.CharField(max_length=40)
    status = models.CharField(max_length=9,null=True)
    meeting_leader = models.CharField(max_length=40)
    documentary = models.CharField(max_length=40)
    first_date = models.CharField(max_length=12)
    final_date = models.CharField(max_length=12)
    first_hour = models.CharField(max_length=10)
    final_hour = models.CharField(max_length=10)

    topics_meeting = models.ManyToManyField(Topic)
    # shedules_meeting = models.OneToOneField(Shedule,on_delete=models.CASCADE)

    def __str__(self):

        return self.project

    def get_absolute_url(self):

        return reverse('meeting-detail', kwargs={'pk': self.pk})