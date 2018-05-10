from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from .forms import EventForm


class MainDashboardView(TemplateView):
    template_name = 'base_home.html'


class EventCreateView(SuccessMessageMixin, CreateView):
    from_class = EventForm
    template_name = 'components-forms.html'
    success_message = "Event has been created successfully"
    success_url = '/event/create/'

    def get_context_data(self, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass




# class MainDashboardView(View):
#
#     def get_c(self, request):
#         return render(request, 'base_home.html')
#
#
# class EventCreateView(SuccessMessageMixin, CreateView):
#     form_class = EventForm
#     template_name = 'components-forms.html'
#     success_message = "Event has been created successfully"
#     success_url = '/event/create/'
#
#     def form_valid(self, form):
#         event = form.save(commit=False)
#         event.save()
#         return super(EventCreateView, self).form_valid(form)

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


