# from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import signup

app_name='accounts'

urlpatterns = [    
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('signup/', signup, name='signup'),
]
