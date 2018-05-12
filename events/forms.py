from django import forms

from .models import EventBasic


class EventForm(forms.ModelForm):
    class Meta:
        model = EventBasic
        fields = '__all__'
        labels = {
            'event_name': 'Event Name',
            'description': 'Description',
            'total_student': 'Total Students',
            'total_trainer': 'Total Trainer',
        }
