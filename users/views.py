from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm  # This is built in Django form. Need with  Django default


def register(request):
    """ If POST request & form has valid fields then create account and return to login page. Otherwise, clear form
        and render register page"""
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)  # Populate data in the User tables using Django default
        form = UserRegisterForm(request.POST)    # Populate data in the User tables using custom form
        if form.is_valid():
            form.username = form.cleaned_data.get('username')
            form.first_name = form.cleaned_data.get('first_name')
            form.last_name = form.cleaned_data.get('last_name')
            form.email = form.cleaned_data.get('email')
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,  # This is to find image
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.username = u_form.cleaned_data.get('username')
            u_form.first_name = u_form.cleaned_data.get('first_name')
            u_form.last_name = u_form.cleaned_data.get('last_name')
            u_form.email = u_form.cleaned_data.get('email')
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required()
def logout(request):
    u_form = UserUpdateForm(instance=request.user)

    auth.logout(request)
    messages.success(request, f'You have been logged out! Do you want to login again?')
    return redirect('login')
