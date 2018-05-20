# Generated by Django 2.0.5 on 2018-05-20 13:38

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('registration_deadline', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('banner', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='media/event_img/'), upload_to='')),
                ('audience_type', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('max_audience', models.IntegerField(default=0)),
                ('venue', models.CharField(max_length=150)),
                ('venue_coordinate', models.CharField(max_length=100)),
                ('region', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('currency', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('registration_fee', models.FloatField(null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('open_for_all', models.BooleanField(default=False)),
                ('screening_process', models.URLField(blank=True, max_length=100, null=True)),
                ('registration_process', models.TextField(default='')),
                ('payment_process', models.URLField(blank=True, max_length=150, null=True)),
                ('additional_fees', models.FloatField(null=True)),
                ('review_event_host', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_complete', models.BooleanField(default=False)),
                ('is_selection_pass', models.BooleanField(default=False)),
                ('payment_confirmed', models.BooleanField(default=False)),
                ('review_participant', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('rating_participant', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('confirmation_text', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('participant_status', models.BooleanField(default=True)),
                ('event_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.EventDetail')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_participant', related_query_name='participant', to='userprofile.PersonalProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0, max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('event_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.EventDetail')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_trainer', related_query_name='trainer', to='userprofile.PersonalProfile')),
            ],
        ),
    ]
