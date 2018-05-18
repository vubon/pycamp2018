from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from  .models.job_post_basic import JobPostBasic
from  .models.job_post_detail import JobPostDetails
from  .models.job_applicant import JobApplicant

from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .froms import JobPostBasicForm,JobPostDetailsForm

class JobDashboardView(View):

    def get(self, request):
        return render(request, 'jobpost/job_post_deshboard.html')

@login_required(login_url='/signin/')
def JobCreate(request):
    user = request.user
    if request.method == 'POST':
        print("Hello........")
        basic_form = JobPostBasicForm(request.POST)
        detail_form = JobPostDetailsForm(request.POST)


        if all([basic_form.is_valid(), detail_form.is_valid()]):
            basic_job_post = basic_form.save(commit=False)
            basic_job_post.organization_id = user
            basic_job_post.save()
            details_job_post = detail_form.save(commit=False)
            details_job_post.job_id = basic_job_post
            details_job_post.save()
            return redirect('jobHome')

    basic_form = JobPostBasicForm(instance=request.user)
    detail_form = JobPostDetailsForm()
    return render(request, 'jobpost/job_post_create.html',
{'basic_form': basic_form, 'detail_form': detail_form})


@method_decorator(login_required, name='dispatch')
class JobListView(ListView):
    model = JobPostBasic


@method_decorator(login_required, name='dispatch')
class JobDetailView(DetailView):
    model = JobPostBasic

@method_decorator(login_required, name='dispatch')
class JobDeleteView(DeleteView):
    model = JobPostBasic
    success_url = reverse_lazy('joblist')

class JobApplicantListView(ListView):
    model = JobApplicant
   # print(queryset)
    template_name = 'jobpost/job_list.html'



def job_applicant(request,pk):
    user=request.user
    job=get_object_or_404(JobPostBasic, pk=pk)
    job_app=JobApplicant(applicant_id=user,job_id=job)
    job_app.save()

    return redirect('joblist')
    # print(user)
    # print(job)


