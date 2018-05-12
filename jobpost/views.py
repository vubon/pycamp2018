
from django.shortcuts import render,redirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from  .models.job_post_basic import JobPostBasic
from  .models.job_post_detail import JobPostDetails

from userprofile.models.organization_profile import OrganizationProfile
from django.contrib.messages.views import SuccessMessageMixin
from .froms import JobPostBasicForm,JobPostDetailsForm
class JobDashboardView(View):

    def get(self, request):
        return render(request, 'jobpost/job_post_deshboard.html')

#
#
# class JobPostCreateView(SuccessMessageMixin, View):
#     basic_form = JobPostBasicForm()
#     detail_form = JobPostDetailsForm()
#     template_name = 'jobpost/job_post_create.html'
#     success_message = "Job has been created successfully"
#     success_url = 'job/jobHome/'
#
#     # def form_valid(self, form):
#     #     job = form.save(commit=False)
#     #     job.save()
#     #     return super(JobPostCreateView, self).form_valid(form)
#
#     def get(self, request):
#         # self.basic_form = EventBasicForm()
#
#         return render(request, self.template_name, {"basic_form": self.basic_form,
#
#                                                  "detail_form": self.detail_form,})
#     # def form_valid(self, form):
#     #     job = form.save(commit=False)
#     #     job.save()
#     #     return super(JobPostCreateView, self).form_valid(form)
#
#     def post(self, request):
#
#         f = JobPostBasicForm(request.POST,instance=request.user)
#         f2=JobPostDetailsForm(request.POST,instance=request.user)
#
#
#
#         if f.is_valid() and f2.is_valid():
#
#             f.save()
#             f2.save()
#
#             return render(request, self.template_name, {"basic_form": self.basic_form,
#
#                                                  "detail_form": self.detail_form,})


# class JobPostBasicCreateView(CreateView):
#     fields = ("job_title", "salary_range", "is_part_time", "position", "stack", "vacancy", "deadline")
#     model = JobPostBasic
#     # fields=("description", "application_process", "screening_details")
#     # model=JobPostDetails
#
# class JobPostDetailsCreateView(CreateView):
#     fields = ("description", "application_process","screening_details")
#     model = JobPostDetails



def JobCreate(request):
    user = request.user
    if request.method == 'POST':
        print("Hello........")
        basic_form = JobPostBasicForm(request.POST)
        detail_form = JobPostDetailsForm(request.POST)


        if all([basic_form.is_valid(), detail_form.is_valid()]):
            basic_job_post = basic_form.save(commit=False)
            basic_job_post.organizationprofile = user
            basic_job_post.save()
            details_job_post = detail_form.save(commit=False)
            details_job_post.jobpostbasic = basic_job_post
            details_job_post.save()
            return redirect('jobHome')

    basic_form = JobPostBasicForm(instance=request.user)
    detail_form = JobPostDetailsForm()
    return render(request, 'jobpost/job_post_create.html',
{'basic_form': basic_form, 'detail_form': detail_form})