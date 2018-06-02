from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import Http404
from  .models.job_post_basic import JobPostBasic
from  .models.job_post_detail import JobPostDetails
from .models.job_applicant import JobApplicant
from userprofile.models.user_profile_basic import UserProfileBasic

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import JobPostBasicForm,JobPostDetailsForm




def indexView(request):
    return render(request, 'jobpost/job_post_dashboard.html')

def listView(request):
    return render(request,'jobpost/job_post_dashboard.html',{'job_list':JobPostBasic.objects.get_job_title(),'userbasic':user_type, 'basic_user':user.id})

def detailJobView(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)

    basic = get_object_or_404(JobPostBasic, id=id)
    detail = get_object_or_404(JobPostDetails,id=id)
    try:
        applicant_object = JobApplicant.objects.get_job_applicant(id,user.id)
        status = True
    except:
        status = False
    return render(request,'jobpost/jobpostbasic_detail.html',{'basic':basic,'detail':detail,'status':status,'userbasic':user_type, 'basic_user':user.id})

def createJobView(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
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
    return render(request, 'jobpost/job_post_create.html', {'basic_form': basic_form, 'detail_form': detail_form,'user':user,'userbasic':user_type, 'basic_user':user.id})


def updateView(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
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

    return render(request, 'jobpost/job_post_edit.html', {'basic_form': basic_form, 'detail_form': detail_form,'userbasic':user_type, 'basic_user':user.id})

def deleteView(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
    basic_object = get_object_or_404(JobPostBasic,id=id)
    basic_object.status = False
    basic_object.save()
    return render(request,'jobpost/job_post_dashboard.html',{'job_list':JobPostBasic.objects.job_title(),'userbasic':user_type, 'basic_user':user.id})

def myJobView(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
    job_list = JobPostBasic.objects.get_my_job(id)
    all_job = JobPostBasic.objects.get_job_title()
    print(job_list)
    return render(request,'jobpost/my_job_list.html',{'job_list':job_list,'all_job':all_job,'userbasic':user_type,'basic_user':user.id})

def jobApplyView(request,id):
    user=request.user
    obj, created = JobApplicant.objects.update_or_create(applicant_id=user.id,job_id=id,apply_status=True)
    print(obj.apply_status)
    return redirect('jobpost:detail',id=id)

def myAppliedJob(request):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
    applied_job = JobApplicant.objects.get_applied_job(user.id)
    return render(request, 'jobpost/my_applied_job.html',{'job_list':applied_job,'userbasic':user_type, 'basic_user':user.id})

def myApplicantView(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
    job_list = JobPostBasic.objects.get_my_job(user.id)
    print(job_list)
    return render(request,'jobpost/my_applicant_list.html',{'job_list':job_list,'userbasic':user_type, 'basic_user':user.id})

def myApplicantList(request,id):
    user = request.user
    user_type = UserProfileBasic.objects.get_organization_status(request.user.id)
    applicant_list = JobApplicant.objects.get_applicant_list(id)
    return render(request,'jobpost/applicant_list.html',{'applicant_list':applicant_list,'userbasic':user_type, 'basic_user':user.id})
