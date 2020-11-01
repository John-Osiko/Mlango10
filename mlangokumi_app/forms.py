from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

from .models import Profile, Neighbourhood, Updates, Business, EmergencyContact, Post


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'age', 'contact', 'address', 'estate', 'role']


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'location', 'image']


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'contact', 'description']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'location', 'owner']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']


class UpdatesForm(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['title', 'tag', 'editor', 'estate', 'up_date']


class UpdateProfileForm(forms.ModelForm):
    profile_pic = ImageField(label='')
    class Meta:
        model = Profile
        fields = ['name', 'age', 'profile_pic', 'contact', 'address', 'estate', 'role']
