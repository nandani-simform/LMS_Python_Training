from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  CustomLoginForm, CustomRegisterForm, UserProfileForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class ProfileView(View):
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request):
        # return render(request, self.template_name)
        u_form = UserUpdateForm(user=request.user)
        p_form = UserProfileForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, user=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            # Update user data
            request.user.username = u_form.cleaned_data['username']
            request.user.email = u_form.cleaned_data['email']
            request.user.save()
            
            # Update profile data
            profile = p_form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(request, 'Your Account has been updated!')
            return redirect(self.success_url)

class CustomLoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        form = CustomLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully logged in.')
                return redirect('first-page')  # Redirect to a success page
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, self.template_name, {'form': form})
    

class CustomLogoutView(View):
    template_name = 'users/logout.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

  
class CustomRegistrationView(View):
    template_name = 'users/register.html'

    def get(self, request):
        form = CustomRegisterForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = CustomRegisterForm(request.POST)
        # profile_form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
        # if form.is_valid() and profile_form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # profile_image = form.cleaned_data['profile_picture']
           
            # create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            # user_profile = Profile(user=user, profile_picture=profile_image)
            # user_profile.save()

            messages.success(request, 'Your account has been created successfully.')
            return redirect('login')
        
        return render(request, self.template_name, {'form':form, })
        # return render(request, self.template_name, {'form':form, 'profile_form':profile_form})
    
