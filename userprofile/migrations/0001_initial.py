# Generated by Django 2.0.5 on 2018-05-13 13:08

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=11)),
                ('current_address', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('gravatar', models.CharField(max_length=100)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('organization_name', models.CharField(max_length=100)),
                ('is_training_institute', models.BooleanField(default=True)),
                ('industry_type', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('website', models.URLField(max_length=100)),
                ('founded_on', models.DateField()),
                ('company_size', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_contact', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=11)),
                ('current_address', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('gravatar', models.CharField(max_length=100)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('about', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('is_trainer', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('education', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('experience', models.CharField(blank=True, choices=[('entry', 'Entry Level'), ('1-2', '1-2 years'), ('3-5', '3-5 years'), ('6-10', '6-10 years'), ('above 10', 'Above 10 years')], max_length=20, null=True)),
                ('permanent_address', models.TextField(max_length=1000)),
                ('interest', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('current_organization', models.TextField(max_length=100)),
                ('official_contact', models.TextField()),
                ('reference', models.TextField()),
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
