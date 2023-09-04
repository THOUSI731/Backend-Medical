from rest_framework.views import APIView
from authentication.models import User
from .serializers import UserListSerializer,UserUpdateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.renderers import AdminRenderer

class UserListAPIView(APIView):
     # renderer_classes=[AdminRenderer]
     # permission_classes = [IsAuthenticated]
     def get(self,request,format=None):
          user = User.objects.all()
          serializer = UserListSerializer(user,many=True)
          return Response(serializer.data,status=status.HTTP_200_OK)
     

class UserUpdateAPIView(APIView):
     permission_classes = [IsAuthenticated,IsAdminUser]
     def get(self,request,pk=None,format=None):
          user_profile=User.objects.filter(id=pk).first()
          serializer=UserUpdateSerializer(user_profile)
          return Response(serializer.data,status=status.HTTP_200_OK)
     
     def patch(self,request,pk=None,format=None):
          user_profile=User.objects.filter(id=pk).first()
          serializer = UserUpdateSerializer(user_profile,data=request.data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response({"msg":"User Updated Successfully"},status=status.HTTP_200_OK)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self,request,pk=None,format=None):
          user_profile=User.objects.filter(id=pk).first()
          if user_profile is not None:
               user_profile.delete() 
               return Response({"msg":"User Deleted Succeffully"},status=status.HTTP_204_NO_CONTENT)
          return Response({"msg":"The User is does not exist"},status=status.HTTP_404_NOT_FOUND)
               
          
          
          