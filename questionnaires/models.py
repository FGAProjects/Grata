from django.db import models

from meetings.models import Meeting
from questions.models import Question

class Quiz(models.Model):

    description = models.CharField(max_length=60)

    questionnaires_meeting = models.ForeignKey(Meeting, null=True, blank=True, on_delete=models.CASCADE)

    question_questionnaires = models.ManyToManyField(Question)