# Generated by Django 2.1.4 on 2019-01-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0001_initial'),
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='questionnaires_meeting',
            field=models.ManyToManyField(to='questionnaires.Quiz'),
        ),
    ]