from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
import requests

class UserView(APIView):
    def get(self,request, pk=None, format=None):
        id = pk
        if id is not None: 
            userobj = CustomUser.objects.get(id=pk)
            user_serializer = UserSerializer(userobj)
            return Response(user_serializer.data)
        userobj = CustomUser.objects.order_by('id')
        user_serializer = UserSerializer(userobj, many=True)
        return Response(user_serializer.data)

    def put(self,request, pk, format=None):
        id = pk
        userobj = CustomUser.objects.get(id=pk)
        user_serializer = UserSerializer(userobj, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'User data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request, pk, format=None):
        id = pk
        userobj = CustomUser.objects.get(id=pk)
        user_serializer = UserSerializer(userobj, data=request.data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'User partial data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userobj = CustomUser.objects.get(id=pk)
        userobj.delete()
        return Response({'message':'User deleted'})

class UserDetailsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # serializer_class = UserSerializer

    def get(self, request):

        print(request.user)
        print(self.request.user)
        # print("request.user")
        user_data = {
            'id' : request.user.id,
            'username' : request.user.username,
            # 'role': request.user.role,

        }
        # user = request.user
        # serializer = UserSerializer(user)

        return Response(user_data, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request):
        user_serializer = UserRegisterSerializer(data = request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response(
                {
                    'user_id': user.id,
                    'username' : user.username,
                    'message': 'Data created',
                }, status=status.HTTP_201_CREATED
            )
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    # permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(token.key)
            return Response({'message': 'Successfully logged in'},status=status.HTTP_200_OK)
        else:
            return Response({'details': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     request.auth.delete()
    #     return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)


