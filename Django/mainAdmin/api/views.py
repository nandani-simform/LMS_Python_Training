from .models import Students
from .serializers import StudentSerializers
from rest_framework import viewsets    
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly , IsAdminUser
from api.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .mypagination import MyPageNumberPagination

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers
    pagination_class = MyPageNumberPagination

    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [JWTAuthentication]


    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
  