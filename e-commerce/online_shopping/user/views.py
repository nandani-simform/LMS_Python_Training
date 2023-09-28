from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserAPI(APIView):
    def get(self,request, pk=None, format=None):
        # id = pk
        if id is not None:
            userobj = CustomUser.objects.get(id=pk)
            user_serializer = UserSerializer(userobj)
            return Response(user_serializer.data)
        userobj = CustomUser.objects.all()
        user_serializer = UserSerializer(userobj, many=True)
        return Response(user_serializer.data)
    
    def post(self, request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'User created'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk, format=None):
        # id = pk
        userobj = CustomUser.objects.get(id=pk)
        user_serializer = UserSerializer(userobj, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'User data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request, pk, format=None):
        # id = pk
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


# class UserListView(ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [BasicAuthentication]    


# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [IsAuthenticated]


