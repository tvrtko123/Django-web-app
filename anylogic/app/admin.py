from django.contrib import admin
from app.models import *

# Register your models here.

model_list = [User, Profil, Post, Kategorija, Homepage]
admin.site.register(model_list)