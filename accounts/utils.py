from rest_framework_simplejwt.tokens import OutstandingToken
from .models import User

def invalidate_tokens(user:User):
    outstanding_tokens = OutstandingToken.objects.filter(user=user)
    outstanding_tokens.delete()
