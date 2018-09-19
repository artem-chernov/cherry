from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login', auth_views.login,{'template_name':'login.html'},name='login')
]
