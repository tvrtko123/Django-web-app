from django.db import models
#from django.contrib.auth.models import User
from app.validators import *
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from django.core.validators import FileExtensionValidator
from django.db.models.fields import DateTimeField
from django.utils import timezone

# Create your models here.

class Homepage(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="images/homepage/")
    opis = models.CharField(max_length=3096, blank=True)

class User(AbstractUser):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

class Profil(models.Model):
    username = models.OneToOneField(User, default=None, null=True, unique=True, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, null=False, default='images/profile/default.jpg', upload_to="images/profile/")
    opis = models.CharField(max_length=200, blank=True)
    datum = models.DateField(default=timezone.now)
    
    @receiver(post_save, sender=User)
    def create_username_profil(sender, instance, created, **kwargs):
        if created:
            Profil.objects.create(username=instance)
            
    @receiver(post_save, sender=User)
    def save_username_profil(sender, instance, **kwargs):
        instance.profil.save()
        
    def __str__(self):
        return "%s" % self.username

class Kategorija(models.Model):
    naziv = models.CharField(unique=True, validators=[isalphavalidator], max_length=30)

    def __str__(self):
        return self.naziv

class Post(models.Model):
    naslov = models.CharField(max_length=30)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ForeignKey(
        Profil,
        null=False,
        default=1,
        on_delete=models.CASCADE
    )
    embed = models.URLField(unique=True, validators=[correctURLvalidator], max_length=100, default='www.anylogic.com')
    opis = models.CharField(max_length=3096, blank=True)
    likes = models.ManyToManyField(User, related_name='post', blank=True)
    datum = DateTimeField(default=timezone.now)
    kategorija = models.ForeignKey(Kategorija, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.naslov

    def total_likes(self):
        return self.likes.count()
    
    # @property
    # def kategorijadata(self):
    #     return self.kategorija.naziv