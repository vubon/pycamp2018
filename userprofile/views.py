from django.shortcuts import render, redirect, get_object_or_404
from userprofile.models.user_profile_basic import UserProfileBasic
from .forms import UserProfileBasicForm

# def profile(request):
#     return render(request, 'userprofile/basic_profile.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    basic_profile = get_object_or_404(UserProfileBasic)
    # user = UserProfileBasic.objects.first()
    if request.method == 'POST':
        form = UserProfileBasicForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request, 'basic_profile.html')
    else:
        form = UserProfileBasicForm()
    return(request, 'base_home.html', {'form':form})



