from gc import get_objects
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, get_user_model
User = get_user_model()
#from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.urls import resolve
from django.core.validators import URLValidator, RegexValidator
from django.core.exceptions import ValidationError
import re
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from braces.views import CsrfExemptMixin
from django.views.decorators.http import require_POST
import json
import os
from django.contrib import messages
from django.core.paginator import Paginator
from django_htmx.http import HttpResponseClientRefresh
from django.utils.translation import gettext as _
from django.contrib.auth import (
    get_user_model, login as auth_login,
)

# Create your views here.
def homepage(request):
    homepage = Homepage.objects.get(id='1')
    context = {'homepage':homepage}       
    return render(request, 'homepage.html', context)

def update_homepage(request):
    return render(request, 'update_homepage.html')

def margin_left(request):
    return render(request, 'partials/left_margin.html')

def profile_picture(request, id):
    profil = Profil.objects.get(id=id)
    image = profil.image.path
    context = {'profil':profil, 'image': image}       

    return render(request, 'partials/profile_picture.html', context)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,)
        username = request.user.id
        if form.is_valid():
            profil_form = form.save(commit=False)
            profil_form.profil = Profil.objects.get(username=username)
            profil_form.save()
            return HttpResponse(headers={'HX-Trigger': 'addPostSuccessful'})
                
    else:
        form = PostForm()
    context = {'form': form,}
    context.update(csrf(request))
    return render(request, 'add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST, request.FILES, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse(headers={'HX-Trigger': 'editPostSuccessful'})
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'post': post,}
    context.update(csrf(request))
    return render(request, 'add_post.html', context)

@ require_POST
@method_decorator(csrf_exempt, name='dispatch')
def remove_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    url = reverse_lazy('posts')
    return HttpResponseRedirect(url)


@method_decorator(csrf_exempt, name='dispatch3')
def modal(request):
    return render(request, 'registration/login.html')


def search_model(request):
    search_text = request.POST.get('search')
    posts = Post.objects.filter(naslov__icontains = search_text).order_by('-datum')
    paginator = Paginator(posts, 24)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'posts':posts, 'page_obj':page_obj}
    return render(request, 'partials/search_results.html', context)

def search_model_category(request, kategorija):
    search_text = request.POST.get('search')
    kategorijas_filter = Kategorija.objects.get(naziv=kategorija)
    posts = Post.objects.filter(kategorija=kategorijas_filter).order_by('-datum')
    posts = posts.filter(naslov__icontains = search_text).order_by('-datum')
    paginator = Paginator(posts, 24)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'posts':posts, 'page_obj':page_obj}
    return render(request, 'partials/search_results.html', context)

def search_model_profile(request, profil):
    search_text = request.POST.get('search')
    profil_filter = Profil.objects.get(username=profil)
    posts = Post.objects.filter(profil=profil_filter).order_by('-datum')
    posts = posts.filter(naslov__icontains = search_text).order_by('-datum')
    paginator = Paginator(posts, 24)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'posts':posts, 'page_obj':page_obj}
    return render(request, 'partials/search_results.html', context)


@method_decorator(csrf_exempt, name='dispatch')
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse(headers={'HX-Trigger': 'loginSuccessful'})

    else:
        form = SignUpForm()

    context = {'form': form}
    context.update(csrf(request))

    return render(request, 'registration/register.html', context)


@method_decorator(csrf_exempt, name='dispatch')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return HttpResponse(headers={'HX-Trigger': 'loginSuccessful'})

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    context = {'form': form}
    context.update(csrf(request))
    form.fields['username'].widget.attrs['class'] = "my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
    form.fields['username'].widget.attrs['placeholder'] = "Username"
    return render(request, "registration/login.html", context)


class EmailAuthenticationForm(AuthenticationForm):
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		ogg = User.objects.filter(email=username)

		if '@' in username:
			if username and password:
				self.user_cache = authenticate(username=ogg[0].username,
											   password=password)
				if self.user_cache is None:
					raise forms.ValidationError(
						self.error_messages['invalid_login'],
						code='invalid_login',
						params={'username': self.username_field.verbose_name},
					)
				else:
					self.confirm_login_allowed(self.user_cache)


		else:
			if username and password:
				self.user_cache = authenticate(username=username,
											   password=password)

                                    
class PostProfilList(ListView):
    model = Profil
    ordering = ['username']
    template_name = 'profil_list.html'
    #queryset = Profil.objects.order_by('username')[:1]
    def get_context_data(self):
            self.profil = get_object_or_404(Profil, username=self.kwargs['id'])
            context = super(PostProfilList, self).get_context_data()
            posts = Post.objects.filter(profil=self.profil).order_by('-datum')
            users = User.objects.filter(username=self.profil)

            context = {'posts':posts, 'users':users}
            return context


def post_list(request):
    users = User.objects.all()
    posts = Post.objects.all().order_by('-datum')
    paginator = Paginator(posts, 24)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    posts_all = Post.objects.all()
    kategorijas = Kategorija.objects.all()
    count = Kategorija.objects.annotate(num_posts=models.Count('post'))

    context = {'posts':posts,  'page_obj':page_obj, 'count':count, 'users':users, 'posts_all':posts_all, 'kategorijas':kategorijas}
    context.update(csrf(request))
    return render(request, 'post_list.html', context)


def post_kategorija_list(request, kategorija):
    kategorijas = Kategorija.objects.all()
    posts_all = Post.objects.all()
    kategorijas_filter = Kategorija.objects.get(naziv=kategorija)
    posts = Post.objects.filter(kategorija=kategorijas_filter).order_by('-datum')
    paginator = Paginator(posts, 24)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    count = Kategorija.objects.annotate(num_posts=models.Count('post'))

    context = {'page_obj':page_obj, 'count':count, 'kategorijas_filter':kategorijas_filter, 'posts_all':posts_all, 'kategorijas':kategorijas}
    context.update(csrf(request))
    return render(request, 'post_list.html', context)

def post_list_by_profile(request, profil):
    profil_filter = Profil.objects.get(username=profil)
    posts = Post.objects.filter(profil=profil_filter).order_by('-datum')
    paginator = Paginator(posts, 24)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    posts_all = Post.objects.all()
    kategorijas = Kategorija.objects.all()
    count = Kategorija.objects.annotate(num_posts=models.Count('post'))

    context = {'posts':posts,  'page_obj':page_obj, 'count':count, 'posts_all':posts_all, 'kategorijas':kategorijas, 'profil_filter':profil_filter}
    context.update(csrf(request))
    return render(request, 'post_list.html', context)

def model_run(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}       

    return render(request, 'partials/model_run.html', context)

#@method_decorator(csrf_exempt, name='dispatch')

class PostSettingsView(DetailView):
    model = Post
    template_name = 'post_settings.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostSettingsView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["liked"] = liked
        context.update(csrf(self.request))
        return context

def like_post(request, id):
    if request.method == "POST":
        instance = Post.objects.get(id=id)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save()
            context={'post':instance}
            context.update(csrf(request))
            return render( request, 'partials/likes_area.html', context)
        else:
            instance.likes.remove(request.user)
            instance.save()
            context={'post':instance}
            context.update(csrf(request))
            return render( request, 'partials/likes_area.html', context)

class KategorijaList(ListView):
    model = Kategorija
    template_name = 'partials/kategorija_list.html'

@method_decorator(csrf_exempt, name='dispatch')

def get_user_profile(request, id):
    user = User.objects.get(id=id)
    profil = Profil.objects.get(id=id)
    posts = Post.objects.filter(profil=profil).order_by('-datum')
    context = {'user':user, 'profil': profil, 'posts': posts}
    if request.method == 'GET':
        return render(request, 'profil_list.html', context)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        user_form = UserInfoForm(data, instance=user)
        profile_form = ProfileInfoForm(data, instance=profil)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponse(headers={'HX-Trigger': 'editInfoSuccessful'})
        else:
            user_form = UserInfoForm(instance=user)
            profile_form = ProfileInfoForm(instance=profil)

    context = {'user_form':user_form, 'profile_form': profile_form, 'user':user, 'profil': profil}
    context.update(csrf(request))
    return render(request, 'partials/edit_profile_detail.html', context)

@method_decorator(csrf_exempt, name='dispatch')
def update_profile_info(request, id):
    user = User.objects.get(id=id)
    profil = Profil.objects.get(id=id)
    user_form = UserInfoForm(instance=user)
    profile_form = ProfileInfoForm(instance=profil)
    context = {'user':user, 'profil': profil, 'user_form': user_form, 'profile_form': profile_form,}
    context.update(csrf(request))
    return render(request, 'partials/edit_profile_detail.html', context)

def update_profile_picture(request, id):
    user = User.objects.get(id=id)
    profil = Profil.objects.get(id=id)
    form = PicutreForm(request.POST, request.FILES, instance=profil)
    context = {'profil':profil, 'form': form, 'user': user}
    context.update(csrf(request))
    if request.method == "POST":
        image_path = profil.image.path       
        if form.is_valid():
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return render(request, 'profil_list.html', context)
        else:
            return render(request, 'profil_list.html', context)
    else:
        form = PicutreForm(instance=profil)
    return render(request, 'partials/update_picture.html', context)
    