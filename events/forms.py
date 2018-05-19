from django import forms

from .models import EventDetail, EventParticipant, EventTrainer


# call for DatePickerInput
class DateInput(forms.DateInput):
    input_type = 'date'


class EventDetailForm(forms.ModelForm):

    class Meta:
        model = EventDetail
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
            'registration_fee',

            'open_for_all',
            'screening_process',
            'registration_process',
            'payment_process',
            'additional_fees',
            'review_event_host',
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'registration_deadline': DateInput(),
        }

    labels = {
        'title': 'Event Title',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'registration_deadline': 'Registration Deadline',
        'description': 'Description',
        'banner': 'Banner',
        'audience_type': 'Audience Type',
        'max_audience': 'Max Audience',
        'venue': 'Venue',
        'venue_coordinate': 'Venue Coordinate',
        'region': 'Region',
        'currency': 'Currency',
        'registration_fee': 'Registration Fee',

        'open_for_all': 'Open for all',
        'screening_process': 'Screening Process',
        'Registration Process': 'registration_process',
        'payment_process': 'Payment Process',
        'additional_fees': 'Additional Fees',
        'review_event_host': 'Review Event Host'
    }


class EventTrainerForm(forms.ModelForm):

    class Meta:
        model = EventTrainer
        fields = [
            'trainer',
            'rating',
            'status',
        ]


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
        ]
