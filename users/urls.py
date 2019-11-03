from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.indexView, name='index'),
    path('home/',views.homeView, name='home'),
    path('home/meetings/',views.meetingsView, name='meetings'),
    path('lead/create/',views.leadCreateView, name='lead_create'),
    path('home/meetings/create/',views.meetingCreateView, name='meeting_create'),
    path('converted/',views.convertedView, name='converted'),
    path('closed/',views.closedView, name='closed'),
    path('register/',views.registerView, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^api/', include('users.api.urls')),
]