from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from .models import User
from .serializers import SignUpSerializer
from .permissions import UserPermission
from rest_framework import viewsets

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login')) # 重新導向到登入畫面
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', context={'form': form})

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [UserPermission]
