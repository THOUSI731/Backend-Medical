from rest_framework.response import Response
from rest_framework import serializers
from authentication.models import User


class UserListSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id','email']
          
          
class UserUpdateSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = '__all__'