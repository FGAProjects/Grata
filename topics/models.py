from django.db import models

class Topic(models.Model):

    topic_name = models.CharField(max_length=25,blank=True)