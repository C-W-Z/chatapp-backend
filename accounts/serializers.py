from rest_framework import serializers
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('email', 'password')
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(email=validated_data["email"], password=validated_data["password"])
