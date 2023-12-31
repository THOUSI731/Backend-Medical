from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .api.serializers import UserRegisterationSerializer,MyTokenObtainPairSerializer,UserProfileSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
     routes = [
          'api/token/',
          'api/token/refresh/',
          'api/register/',
     ]
     return Response(routes)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    

class UserRegisterView(APIView):
     def post(self,request,format=None):
          serializer = UserRegisterationSerializer(data=request.data)
          if serializer.is_valid():
               user = User.objects.create(
                    username = serializer.validated_data['username'],
                    first_name = serializer.validated_data['first_name'],
                    last_name = serializer.validated_data['last_name'],
                    email = serializer.validated_data['email'],
                    account_type = serializer.validated_data['account_type']
               )
               user.set_password(serializer.validated_data['password'])
               user.save()
               return Response({'msg':'Registeration Successfull'},status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserHomeView(APIView):  
     def get(self,request,format=None):
          match request.user.account_type:
               case 'user':
                    doctors = User.objects.filter(account_type='doctor')
                    serializer = UserProfileSerializer(doctors,many=True)
                    return Response(serializer.data,status=status.HTTP_200_OK)                    
               case 'doctor':
                    doctor = User.objects.filter(username=request.user).first()
                    serializer = UserProfileSerializer(doctor,many=False)
                    print(serializer)
                    return Response(serializer.data,status=status.HTTP_200_OK)          
          
          
          
class UserProfileView(APIView):
     permission_classes=[IsAuthenticated]
     def get(self,request,format=None):
          serializer= UserProfileSerializer(request.user)
          return Response(serializer.data,status=status.HTTP_200_OK)
     
     def put(self,request,format=None):
          print(request.user)
          try: 
               user_profile = User.objects.get(email=request.user)
          except User.DoesNotExist:
               return Response({"msg":"There is no user put request"},status=status.HTTP_400_BAD_REQUEST)
          serializer = UserProfileSerializer(user_profile,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Profile Updated Successfully',"method":"PUT"})
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
     
     def patch(self,request,format=None):
          try: 
               user_profile = User.objects.get(email=request.user)
          except User.DoesNotExist:
               return Response({"msg":"There is no user"},status=status.HTTP_400_BAD_REQUEST)
          serializer = UserProfileSerializer(user_profile,data=request.data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Profile Updated Successfully',"method":"PATCH"},status=status.HTTP_200_OK)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
          
# from rest_framework.permissions import IsAuthenticated

# class LogoutView(APIView):
#      permission_classes = (IsAuthenticated,)
#      def post(self, request):
          
#           try:
#                refresh_token = request.data["refresh"]
#                token = RefreshToken(refresh_token)
#                token.blacklist()
#                return Response(status=status.HTTP_205_RESET_CONTENT)
#           except Exception as e:
#                return Response(status=status.HTTP_400_BAD_REQUEST)
     
# class UserLoginView(APIView):
#      def post(self,request,format=None):
#           serializer = UserLoginSerializer(data=request.data) 
#           if serializer.is_valid():
#                email = serializer.data.get('email') 
#                password = serializer.data.get('password')
#                print(password)
#                user = User.objects.filter(email=email).first()
#                if user is not None:
#                     if not user.is_blocked:
#                          token = get_tokens_for_user(user)
#                     else:
#                          return Response({"msg":"Your Account is blocked"},status=status.HTTP_401_UNAUTHORIZED)
#                     return Response({"msg":"Login Success","authTokens":token},status=status.HTTP_200_OK)
#                else:
#                     return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_401_UNAUTHORIZED)
#           return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

