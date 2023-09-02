from rest_framework import serializers
from ..models import User,Note
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['is_blocked'] = user.is_blocked

        return token
   
class UserRegisterationSerializer(serializers.ModelSerializer):
     password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
     class Meta:
          model = User
          fields = ['first_name','last_name','username','email','password','password2','account_type']
          extra_kwargs = {
               'password':{'write_only':True}
          }
          
     def validate(self, attrs):
          password = attrs.get('password')
          password2 = attrs.get('password2')
          first_name = attrs.get('first_name')
          last_name = attrs.get('last_name')
          if first_name == last_name:
               raise serializers.ValidationError('First Name And Last Name Can\'t Be Same')
          if password != password2:
               raise serializers.ValidationError('Password Didn\'t Match')
          return attrs
     
class UserLoginSerializer(serializers.ModelSerializer):
     email = serializers.CharField()
     class Meta:
          model = User
          fields = ['email','password']
         
         
class NoteSerializer(serializers.ModelSerializer):
     class Meta:
          model = Note
          fields = '__all__'