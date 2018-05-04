import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainDashBoardView(View):
    def get(self, request):
        return render(request, 'index.html')

class EventCreateView(View):
    template_name = 'components-forms.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass