from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import Http404
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from  .models.job_post_basic import JobPostBasic
from  .models.job_post_detail import JobPostDetails
from .models.job_applicant import JobApplicant

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import JobPostBasicForm,JobPostDetailsForm



def indexView(request):
    return render(request, 'jobpost/job_post_dashboard.html')

def listView(request):
    return render(request,'jobpost/job_post_dashboard.html',{'job_list':JobPostBasic.objects.job_title()})

def detailJobView(request,id):
    user = request.user
    basic = get_object_or_404(JobPostBasic, id=id)
    detail = get_object_or_404(JobPostDetails,id=id)
    try:
        applicant_object = JobApplicant.objects.get_job_applicant(id,user.id)
        status = True
    except:
        status = False
    return render(request,'jobpost/jobpostbasic_detail.html',{'basic':basic,'detail':detail,'status':status})

def createJobView(request,id):
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
    return render(request, 'jobpost/job_post_create.html', {'basic_form': basic_form, 'detail_form': detail_form,'user':user})


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


class JobApplicantListView(ListView):
    model = JobApplicant
   # print(queryset)
    template_name = 'jobpost/jobapplicant_list.html'



# def job_applicant(request,id):
#     user=request.user
#     job=get_object_or_404(JobPostBasic, id=id)
#     job_app=JobApplicant(applicant=user,job=job)
#     job_app.save()
#     return redirect('jobpost:index')

def myJobView(request,id):
    user = request.user
    job_list = JobPostBasic.objects.my_job(id)
    all_job = JobPostBasic.objects.job_title()
    print(job_list)
    # return render(request,'jobpost/my_job_list.html',{'my_job':job_list,'all_job':all_job})
    return render(request,'jobpost/my_job_list.html',{'job_list':job_list,'all_job':all_job})

def jobApplyView(request,id):
    user=request.user
    obj, created = JobApplicant.objects.update_or_create(applicant_id=user.id,job_id=id,apply_status=True)
    print(obj.apply_status)
    return redirect('jobpost:detail',id=id)

def myAppliedJob(request):
    user =request.user
    applied_job = JobApplicant.objects.get_applied_job(user.id)
    return render(request, 'jobpost/my_applied_job.html',{'job_list':applied_job})

def myApplicantView(request,id):
    user = request.user
    job_list = JobPostBasic.objects.my_job(user.id)
    print(job_list)
    return render(request,'jobpost/my_applicant_list.html',{'job_list':job_list})

def myApplicantList(request,id):
    user = request.user
    applicant_list = JobApplicant.objects.get_applicant_list(id)
    return render(request,'jobpost/applicant_list.html',{'applicant_list':applicant_list})
