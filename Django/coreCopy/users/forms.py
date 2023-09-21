from django import forms
from django.contrib.auth.models import User
from .models import Profile


class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomRegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    # profile_image = forms.ImageField(required=False, widget=forms.FileInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        
     
# class UserProfileForm(forms.Form):
#     profile_picture = forms.ImageField(required=False)

#     def clean_profile_picture(self):
#         profile_picture = self.cleaned_data.get('profile_picture')
#         return profile_picture
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']


class UserUpdateForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.user.username
        self.fields['email'].initial = self.user.email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.exclude(pk=self.user.pk).filter(username=username).exists():
            raise forms.ValidationError('Username is already taken.')
        return username
    
    def clean_email(self):
        new_email = self.cleaned_data['email']

        # Check if the new email is the same as the old email
        if new_email == self.user.email:
            return new_email

        # Check if the new email is already taken
        if User.objects.filter(email=new_email).exclude(username=self.user.username).exists():
            raise forms.ValidationError("Email is already associated with another account.")

        return new_email