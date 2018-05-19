from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from  .models.job_post_basic import JobPostBasic
from  .models.job_post_detail import JobPostDetails

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import JobPostBasicForm,JobPostDetailsForm



def indexView(request):
    return render(request, 'jobpost/job_post_dashboard.html')

def listView(request):
    return render(request,'jobpost/job_post_dashboard.html',{'job_list':JobPostBasic.objects.job_title()})

def detailJobView(request,id):
    basic = get_object_or_404(JobPostBasic, id=id)
    detail = get_object_or_404(JobPostDetails,id=id)
    return render(request,'jobpost/jobpostbasic_detail.html',{'basic':basic,'detail':detail})

def createJobView(request):
    user = request.user
    if request.method == 'POST':
        basic_form = JobPostBasicForm(request.POST)
        detail_form = JobPostDetailsForm(request.POST)


        if all([basic_form.is_valid(), detail_form.is_valid()]):
            basic_job_post = basic_form.save(commit=False)
            basic_job_post.organization = user
            basic_job_post.save()
            details_job_post = detail_form.save(commit=False)
            details_job_post.job = basic_job_post
            details_job_post.save()

            return redirect('jobpost:detail',id=basic_job_post.id)
    else:
        basic_form = JobPostBasicForm()
        detail_form = JobPostDetailsForm()
    return render(request, 'jobpost/job_post_create.html', {'basic_form': basic_form, 'detail_form': detail_form})


def updateView(request,id):
    user = request.user
    basic_object = get_object_or_404(JobPostBasic,id=id)
    detail_object = get_object_or_404(JobPostDetails,id=id)
    if request.method == 'POST':
        print(id)
        basic_form = JobPostBasicForm(request.POST,instance=basic_object)
        detail_form = JobPostDetailsForm(request.POST,instance=detail_object)


        if all([basic_form.is_valid(), detail_form.is_valid()]):
            basic_job_post = basic_form.save(commit=False)
            basic_job_post.organization = user
            basic_job_post.save()
            details_job_post = detail_form.save(commit=False)
            details_job_post.job = basic_job_post
            details_job_post.save()

            return redirect('jobpost:detail',id=id)
    else:
        basic_form = JobPostBasicForm(instance=basic_object)
        detail_form = JobPostDetailsForm(instance=detail_object)

    return render(request, 'jobpost/job_post_edit.html', {'basic_form': basic_form, 'detail_form': detail_form})

def deleteView(request,id):
    user = request.user
    basic_object = get_object_or_404(JobPostBasic,id=id)
    basic_object.status = False
    basic_object.save()
    return render(request,'jobpost/job_post_dashboard.html',{'job_list':JobPostBasic.objects.job_title()})
