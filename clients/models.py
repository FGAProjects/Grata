from django.db import models
from django.urls import reverse

class Client(models.Model):

    name = models.CharField(max_length=35)
    ramal = models.CharField(max_length=4)
    sector = models.CharField(max_length=70)
    email = models.CharField(max_length=25)
    permission = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_edit', kwargs={'pk': self.pk})