from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from .forms import EventForm


class MainDashboardView(TemplateView):
    template_name = 'event_templates/event_dashboard.html'


class EventCreateView(SuccessMessageMixin, CreateView):
    form_class = EventForm
    template_name = 'event_templates/event_create.html'
    success_message = "Event has been created successfully"
    success_url = 'event_templates/event_archive/'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return super(EventCreateView, self).form_valid(form)

    # def get(self, request):
    #     form = EventForm()
    #     return render(request, self.template_name, {"form": form})
    #
    # def post(self, request):
    #     f = EventForm(request.POST)
    #     form = EventForm()
    #     if f.is_valid():
    #         f.save()
    #         return render(request, self.template_name, {"form": form})
    #     else:
    #         return render(request, self.template_name, {"error": f.errors})


class EventArchiveView(TemplateView):
    template_name = 'event_templates/event_archive.html'


class OrganizerProfileVew(TemplateView):
    template_name = 'event_templates/organizer_profile.html'


