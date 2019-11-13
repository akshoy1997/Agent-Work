from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('home/',views.homeView, name='home'),
    path('home/meetings/',views.meetingsView, name='meetings'),
    path('lead/create/',views.leadCreateView, name='lead_create'),
    path('home/meetings/create/',views.meetingCreateView, name='meeting_create'),
    path('home/lead/status_update/',views.statusUpdateView, name='status_update'),
    path('home/lead/closed/',views.leadClosedView, name='lead_closed'),
    path('home/lead/converted/',views.leadConvertedView, name='lead_converted'),
    path('converted/',views.convertedView, name='converted'),
    path('closed/',views.closedView, name='closed'),
    path('register/',views.registerView, name='register'),
    path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^api/', include('users.api.urls')),
    url(r'^serviceworker.js', (TemplateView.as_view(template_name="serviceworker.js", content_type='application/javascript', )), name='serviceworker.js'),
]