# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import *
from .forms import SignupForm, NeighbourhoodForm, EmergencyForm, BusinessForm, PostForm, UpdatesForm, UpdateProfileForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        hoods = Neighbourhood.objects.all()
        profiles = Profile.objects.all()
        biz = Business.objects.all()
        emergencies = EmergencyContact.objects.all()
        posts = Post.objects.all()

        index_data = {
            'hoods': hoods,
            'profiles': profiles,
            'businesses': biz,
            'emergencies': emergencies,
            'posts': posts,
            'form': form,
        }

    except Neighbourhood.DoesNotExist:
        hoods = None
        profiles = None
        biz = None
        emergencies = None
        posts = None
    return render(request, 'jirani_temp/index.html', index_data)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = request.user.profile.estate
            post.owner = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'posting/make_posts.html', {'form': form})


@login_required(login_url='login')
def create_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
    else:
        form = NeighbourhoodForm
    return render(request, 'posting/add_hood.html', {'form': form})


@login_required(login_url='login')
def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.save()
    else:
        form = BusinessForm
    return render(request, 'posting/add_business.html', {'form': form})


@login_required(login_url='login')
def create_emergency(request):
    if request.method == 'POST':
        form = EmergencyForm(request.POST, request.FILES)
        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.save()
    else:
        form = EmergencyForm
    return render(request, 'posting/add_emergency.html', {'form': form})


def profile(request, username):
    return render(request, 'jirani_temp/profile.html')




@login_required(login_url='login')
def updates(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    current_updates = updates.objects.filter(estate=profile.estate)

    return render(request, 'jirani_temp/updates.html', {"updates":current_updates})



@login_required(login_url='login')
def new_update(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    if request.method == "POST":
        form = UpdatesForm(request.POST, request.FILES)
        if form.is_valid():
            updates = form.save(commit=False)
            updates.editor = current_user
            updates.estate = profile.estate
            updates.save()

        return HttpResponseRedirect('/updates')

    else:
        form = UpdatesForm()

    return render(request, 'jirani_temp/updates_form.html',locals())


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your Profile account has been updated successfully')
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'jirani_temp/edit_profile.html', {'form': form})


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        print(search_term)
        searched_photos = Neighbourhood.search_by_title(search_term)
        print(searched_photos)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'search.html', params)

    else:
        message = 'Invalid search! Try again.'
        return render(request, 'jirani_temp/search.html', locals())