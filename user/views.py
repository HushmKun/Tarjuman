from django.contrib.auth import login
from django.shortcuts import redirect, render
from user.forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from . import views
from main.models import Post, Tag, Comment

# Create your views here.

@login_required
def dashboard(request):
    user_comments = Comment.objects.all().filter(user=request.user)

    return render(request, "users/index.html", {
        "no_of_comments" : user_comments.count()
    })

def register(request):

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES) 
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)  
            return redirect('dashboard')  
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileUpdateForm()

    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})

