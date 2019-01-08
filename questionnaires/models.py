from django.db import models

class Quiz(models.Model):

    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=4, null=True)
