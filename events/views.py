from django.views import View
from django.shortcuts import render

from .forms import EventForm


class MainDashboardView(View):

    def get(self, request):
        return render(request, 'index.html')


class EventCreateView(View):
    template_name = 'components-forms.html'

    def get(self, request):
        form = EventForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {"form": form})
        else:
            return render(request, self.template_name, {"error": form.errors})

