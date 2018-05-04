from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'event_name': 'Event Name',
            'description': 'Description',
            'total_student': 'Total Students',
            'total_trainer': 'Total Trainer',
        }
