from django import forms
from app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate



class SignUpForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'E-mail'}),
        }

class LoginForm(AuthenticationForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white', 'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'w-4 h-4 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800'}))

    class Meta:
        model = get_user_model()
        fields = ['username']
 

class PostForm(forms.ModelForm):

    #naslov = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full mt-1 mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}))
    #videofile = forms.FileField(widget=forms.FileInput(attrs={'class': 'w-full mb-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5'}))
    #opis = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full h-40 mt-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}))
    #kategorija = forms.ModelMultipleChoiceField(queryset=Kategorija.objects.all(), widget=forms.Select(attrs={'name': 'kategorija', 'id': 'id_kategorija', 'class': 'w-2/3 mt-4 mb-1 ml-3 pl-1 rounded bg-gray-50 border border-gray-300 text-gray-900 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}))   

    class Meta:
        model = Post
        fields = ('naslov', 'embed', 'opis', 'kategorija',)

        widgets = {
            'naslov' : forms.TextInput(attrs={'class': 'w-full mt-1 mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200', 'required': ''}),
            'kategorija': forms.Select(attrs={'name': 'kategorija', 'id': 'id_kategorija', 'class': 'w-2/3 mt-4 mb-1 ml-3 pl-1 rounded bg-gray-50 border border-gray-300 text-gray-900 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200', 'required': ''}),
            'embed': forms.URLInput(attrs={'class': 'w-full mb-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5w-full mt-1 mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200', 'required': ''}),
            'opis' : forms.Textarea(attrs={'class': 'w-full h-40 mt-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}),

        }   

class PicutreForm(forms.ModelForm):

    class Meta:
        model = Profil
        fields = ['image']

        widgets = {
            'image': forms.FileInput(attrs={'required': ''}),
        }   

class ProfileInfoForm(forms.ModelForm):

    class Meta:
        model = Profil
        fields = ['opis']

        widgets = {
            'opis': forms.Textarea(attrs={'class': 'w-full h-40 mt-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}),
        }   

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full mt-1 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full mt-1 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}),
            'email': forms.EmailInput(attrs={'class': 'w-full mt-1 mb-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-slate-200'}),
        }

 
