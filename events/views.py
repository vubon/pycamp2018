from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import EventDetailForm, EventParticipantForm, EventTrainerForm
from userprofile.models import UserProfileBasic, PersonalProfile


from .models import EventDetail, EventTrainer, EventParticipant


class EventDashboardView(LoginRequiredMixin, ListView):
    model = EventDetail
    login_url = '/'
    template_name = 'event_templates/event_dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return EventDetail.objects.filter(owner=self.request.user)


class OrganizerProfileVew(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'event_templates/organizer_profile.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    form_class = EventDetailForm
    login_url = '/'
    # form_participant = EventParticipantForm
    template_name = 'event_templates/event_create.html'
    success_url = '/event/event_trainer/'

    def get(self, request):
        return render(request, self.template_name, {"event_detail": self.form_class})

    def form_valid(self, form):
        instance = form.save(commit=True)
        instance.owner = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventTrainerCreateView(LoginRequiredMixin, CreateView):
    form_class = EventTrainerForm
    login_url = '/'
    template_name = 'event_templates/event_trainer.html'
    success_url = '/event/event_list/'

    def get(self, request):
        return render(request, self.template_name, {"event_trainer": self.form_class})

    def form_valid(self, form):
        instance = form.save(commit=True)
        instance.owner = self.request.user
        return super(EventTrainerCreateView, self).form_valid(form)


"""
# How to use Participants views
class EventParticipantCreateView(LoginRequiredMixin, CreateView):
    form_class = EventParticipantForm
    login_url = '/'
    template_name = 'event_templates/event_participant.html'
    success_url = '/event/event_list/'

    def get(self, request):
        return render(request, self.template_name, {"event_participant": self.form_class})

    def form_valid(self, form):
        instance = form.save(commit=True)
        instance.owner = self.request.user
        return super(EventParticipantCreateView, self).form_valid(form)
"""


class EventListView(LoginRequiredMixin, ListView):
    login_url = '/'
    model = EventDetail
    template_name = 'event_templates/event_archive.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return EventDetail.objects.filter(owner=self.request.user)


class EventDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'
    model = EventDetail
    template_name = 'event_templates/single_event.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['event_trainer'] = EventTrainer.objects.all()
        context['event_participants'] = EventParticipant.objects.all()
        return context


class EventDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = EventDetail
    form_class = EventDetailForm
    login_url = '/'
    template_name = 'event_templates/event_update.html'
    success_url = '/event/event_list/'
    print(form_class)

    def get_queryset(self):
        return EventDetail.filter(user=self.request.user)

    def get(self, request, slug):
        return render(request, self.template_name, {"event_detail": self.form_class})

    # def get_context_data(self, *args, **kwargs):
    #     context = super(EventDetailUpdateView, self).get_context_data(*args, **kwargs)
    #     return context

    # def form_valid(self, form):
    #     instance = form.save(commit=True)
    #     instance.owner = self.request.user
    #     return super(EventCreateView, self).form_valid(form)
    #
    # def get_form_kwargs(self):
    #     kwargs = super(EventCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


class EventDeleteView(DeleteView):
    model = EventDetail
    template_name = 'event_templates/eventdetail_confirm_delete.html'
    success_url = reverse_lazy('event_list')


def event_apply(request, slug):
    user = request.user
    event = get_object_or_404(EventDetail, slug=slug)
    event_app = EventParticipant(participant_id=user, event_title=event)
    event_app.save()

    return redirect('participant_list')


class EventParticipantList(LoginRequiredMixin, ListView):
    model = EventParticipant
    template_name = 'event_templates/participant_list.html'
