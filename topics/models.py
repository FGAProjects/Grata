from django.db import models

from meetings.models import Meeting

class Topic(models.Model):

    topic_name = models.CharField(max_length=25)