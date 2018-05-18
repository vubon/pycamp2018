# Generated by Django 2.0.5 on 2018-05-14 20:47

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventdetail_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='eventparticipant',
            managers=[
                ('participant', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='payment_process',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='screening_process',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='title',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='venue',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='venue_coordinate',
            field=models.CharField(max_length=100),
        ),
    ]
