# main/urls.py

from django.urls import include, path, re_path
from django.contrib.auth.views import LoginView
#from rest_framework import routers
from . import views
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views


#router = routers.DefaultRouter()
#router.register(r'korisnici', views.KorisnikViewSet)

urlpatterns = [
    path('', views.homepage, name='home'),
    path('margin_left', views.margin_left, name='margin_left'),
    path('profile_picture/<id>/', views.profile_picture, name='profile_picture'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('', AddURLView.as_view(), name='add_url'),
    path('registration/', views.registration, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('profile/<id>/', views.get_user_profile, name='profile'),
    path('profile/<id>/update_info/', views.update_profile_info, name='update_profile_info'),
    path('profile/<id>/update_picture/', views.update_profile_picture, name='update_profile_picture'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', views.post_list, name='posts'),
    path('posts/<profil>', views.post_list_by_profile, name='post_list_by_profile'),
    path('post/<pk>', views.model_run, name='model_run'),
    path('post/<pk>/settings', PostSettingsView.as_view(), name='post_settings'),
    path('add_post/', views.add_post, name='add_post'),
    path("kategorijas/", KategorijaList.as_view()),
    path('posts/<kategorija>/', views.post_kategorija_list, name='kategorija_filter'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset_<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
htmx_urlpatterns = [
    path('like/<uuid:id>', views.like_post, name='like_post'),
    path('search_model', views.search_model, name='search_model'),
    path('search_model_category/<kategorija>', views.search_model_category, name='search_model_category'),
    path('search_model_profile/<profil>', views.search_model_profile, name='search_model_profile'),
    path('modal', views.modal, name='modal'),
    #path('copy_modal/<pk>', views.copy_modal, name='copy_modal'),
    path('add_post', views.add_post, name='add_post'),
    path('post/<pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<pk>/remove', views.remove_post, name='remove_post'),

]

urlpatterns += htmx_urlpatterns
