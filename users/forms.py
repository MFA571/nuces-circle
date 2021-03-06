from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Education, Interests, Skills, WorkExperience, Recruiter


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class FBRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]


class UserRegisterForm(UserCreationForm):  # inheriting from UserCreationForm
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.EmailField()  # by def required is true
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    username.help_text = ''
    email.help_text = ''
    password1.help_text = ''
    password1.label = 'Password'
    password2.label = 'Confirm Password'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class RecruiterRegForm(forms.ModelForm):
    company = forms.CharField(required=True)
    industry = forms.CharField(required=True)

    class Meta:
        model = Recruiter
        fields = ['company', 'industry']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'grad_year', 'study_field', 'description']
        labels = {
            'grad_year': 'Graduation Year'
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['exp_title', 'company', 'description', 'start_year', 'end_year']
        labels = {
            'exp_title': 'Title',
            'start_year': 'Start Date',
            'end_year': 'End Date'
        }


class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ['frameworks', 'languages', 'technologies']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']
