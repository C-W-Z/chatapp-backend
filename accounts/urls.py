# from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import CustomTokenObtainPairView# ,signup,CustomAuthToken
from rest_framework.routers import DefaultRouter
from accounts import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name='accounts'

router = DefaultRouter()
router.register(r"signup", views.SignUpViewSet, basename="signup")

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/token/', CustomAuthToken.as_view(), name='token_obtain_pair'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    # path('signup/', signup, name='signup'),
]
