# from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import signup, CustomAuthToken
from rest_framework.routers import DefaultRouter
from accounts import views

app_name='accounts'

router = DefaultRouter()
router.register(r"signup", views.SignUpViewSet, basename="signup")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', CustomAuthToken.as_view(), name='token_obtain_url'),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    # path('signup/', signup, name='signup'),
]
