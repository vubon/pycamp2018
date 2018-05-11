from django import forms

from django.contrib.postgres.fields import JSONField
# from django.core.files.storage import FileSystemStorage

from .models import EventBasic, EventParticipant, EventDetail, EventTrainer


class EventBasicForm(forms.ModelForm):

    class Meta:
        model = EventBasic
        fields = [
            'title',
            'start_date',
            'end_date',
            'registration_deadline',
            'description',
            'banner',
            'audience_type',
            'max_audience',
            'venue',
            'venue_coordinate',
            'region',
            'currency',
            'registration_fee'
        ]

        # def __init__(self, *args, **kwargs):
        #     super(EventBasicForm, self).__init__(*args, **kwargs)
        #     self.fields['title'].widget.attrs['class'] = 'my_class'


# class EventForm(forms.ModelForm):
#     class Meta:
#         model = EventBasic
#         fields = '__all__'
#         labels = {
#             'event_name': 'Event Name',
#             'description': 'Description',
#             'total_student': 'Total Students',
#             'total_trainer': 'Total Trainer',
#         }


class EventParticipantForm(forms.ModelForm):

    class Meta:
        model = EventParticipant
        fields = [
            'participant_id',
            'registration_complete',
            'is_selection_pass',
            'payment_confirmed',
            'review_participant',
            'rating_participant',
            'confirmation_text',
            'participant_status',
            # 'participant',
        ]


class EventDetailForm(forms.ModelForm):

    class Meta:
        model = EventDetail
        fields = [
            # 'title',
            # 'start_date',
            # 'end_date',
            # 'registration_deadline',
            # 'description',
            # 'banner',
            # 'audience_type',
            # 'max_audience',
            # 'venue',
            # 'venue_coordinate',
            # 'region',
            # 'currency',
            # 'registration_fee',

            'open_for_all',
            'screening_process',
            'registration_process',
            'payment_process',
            'additional_fees',
            'review_event_host'
        ]


class EventTrainerForm(forms.ModelForm):

    class Meta:
        model = EventTrainer
        fields = [
            'trainer',
            'rating',
            'status'
        ]