# Generated by Django 2.0.5 on 2018-05-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_total_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='total_trainer',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
