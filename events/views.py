from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from .forms import EventForm


class MainDashboardView(View):

    def get(self, request):
        return render(request, 'index.html')


class EventCreateView(SuccessMessageMixin, CreateView):
    form_class = EventForm
    template_name = 'components-forms.html'
    success_message = "Event has been created successfully"
    success_url = '/event/create/'

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

