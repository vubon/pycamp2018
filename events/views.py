from django.views import View
# from django.views.generic import CreateView
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from .forms import EventBasicForm, EventDetailForm, EventParticipantForm, EventTrainerForm


class MainDashboardView(TemplateView):
    template_name = 'event_templates/event_dashboard.html'


class EventCreateView(SuccessMessageMixin, CreateView):
    template_name = 'event_templates/event_create.html'
    success_message = "Event has been created successfully"
    success_url = 'event_templates/event_archive/'

    basic_form = EventBasicForm()
    basic_form.prefix = 'basic_form'
    detail_form = EventDetailForm()
    detail_form.prefix = 'detail_form'
    trainer_form = EventTrainerForm()
    trainer_form.prefix = 'trainer_form'
    participant_form = EventParticipantForm()
    participant_form.prefix = 'participant_form'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return super(EventCreateView, self).form_valid(self.form)

    def get(self, request):
        # self.basic_form = EventBasicForm()
        return render(request, self.template_name, {"basic_form": self.basic_form,
                                                    "detail_form": self.detail_form,
                                                    "participant_form": self.participant_form,
                                                    "trainer_form": self.trainer_form})

    def post(self, request, *args, **kwargs):
        basic_form = EventBasicForm(self.request.POST, prefix='basic_form')
        detail_form = EventDetailForm(self.request.POST, prefix='detail_form')
        participant_form = EventTrainerForm(self.request.POST, prefix='participant_form')
        trainer_form = EventParticipantForm(self.request.POST, prefix='trainer_form')

        if basic_form.is_valid():
            basic_form.save()
            return render(request, self.template_name, {'basic_form': basic_form})
        else:
            return render(request, self.template_name, {"error": basic_form.errors})


class EventArchiveView(TemplateView):
    template_name = 'event_templates/event_archive.html'


class OrganizerProfileVew(TemplateView):
    template_name = 'event_templates/organizer_profile.html'


