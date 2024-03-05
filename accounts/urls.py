# from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name='accounts'

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/signup/', views.SignUpView.as_view(), name='signup'),
    path('api/logout/', views.LogOutView.as_view(), name='logout'),
    path('api/profile/', views.UserProfileView.as_view(), name='profile'),
    path('api/username/', views.UserNameView.as_view(), name='username'),
]
