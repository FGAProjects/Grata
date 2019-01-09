from django.db import models

from questionnaires.models import Quiz

class Answer(models.Model):

    answer_for_question = models.CharField(max_length=4)

    answer_question = models.ForeignKey(Quiz, null=True, blank=True, on_delete=models.CASCADE)
