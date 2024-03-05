from .models import User, UserProfile
from .serializers import SignUpSerializer, CustomTokenObtainPairSerializer, UserNameSerializer, UserProfileSerializer
from .utils import invalidate_tokens
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

# POST: signup User
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password1 = serializer.validated_data.get('password')
        password2 = request.data.get('password2')

        if password1 != password2:
            return Response({'password2': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# POST: delete all tokens of the User
class LogOutView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        invalidate_tokens(user=self.request.user)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

# GET/PUT/PATCH User.username
class UserNameView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserNameSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user

# GET/PUT/PATCH UserProfile
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Get Profile.user (e.g. for authentication)
        return self.queryset.get(user=self.request.user)
