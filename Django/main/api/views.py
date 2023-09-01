from django.shortcuts import render
from .models import Students
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import io
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator 
from rest_framework import status, viewsets
from rest_framework.views import APIView

from rest_framework.generics import (GenericAPIView, 
                                     ListAPIView, 
                                     CreateAPIView, 
                                     UpdateAPIView, 
                                     DestroyAPIView, 
                                     RetrieveAPIView, 
                                     ListCreateAPIView, 
                                     RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                    )
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# def student_detail(request, pk):
#     stu = Students.objects.get(id = pk)
#     serializer = StudentSerializers(stu)

#     json_data = JSONRenderer().render(serializer.data)

#     return HttpResponse(json_data, content_type = 'application/json')


# def student_detail_list(request):

#     stu = Students.objects.all()
#     serializer = StudentSerializers(stu, many=True)
#     json_data = JSONRenderer().render(serializer.data)

#     return HttpResponse(json_data, content_type = 'application/json')
 

# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPI(View):

#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata =  JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Students.objects.get(id=id)
#             serializer =  StudentSerializers(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = 'application/json')
    
#         stu = Students.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = 'application/json')
    
#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
        
#         serializer = StudentSerializers(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application/json')

#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
        
#         id = pythondata.get('id')
#         stu = Students.objects.get(id=id)

#         serializer = StudentSerializers(stu, data=pythondata, partial = True)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application/json')

#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)

#         id = pythondata.get('id')
#         stu = Students.objects.get(id=id)

#         stu.delete()
#         res = {'msg': 'Data deleted !!'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type = 'application/json')        

#         return JsonResponse(res, safe=False)    

# CRUD api using FBV
# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Students.objects.get(id=id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data)
        
#         stu = Students.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Data created!!"})
#         return Response(serializer.errors)
    

#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data updated!!'})
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Students.objects.get(pk=id)

#         stu.delete()
#         return Response({'msg':'Data deleted!!'})


# Function based API VIEW
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request, pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Students.objects.get(id=id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data)
        
#         stu = Students.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Data created!!"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':
#         id = pk
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data updated!!'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PATCH':
#         id = pk
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data updated!!'})
#         return Response(serializer.errors)

#     if request.method == 'DELETE': 
#         id = pk
#         stu = Students.objects.get(pk=id)

#         stu.delete()
#         return Response({'msg':'Data deleted!!'})


# #class based view
# class StudentAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             stu = Students.objects.get(id=id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data)
        
#         stu = Students.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = StudentSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Data created!!"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         id = pk
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data updated!!'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, pk, format=None):
#         id = pk
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data updated!!'})
#         return Response(serializer.errors)


#     def delete(self, request, pk, format=None):
#         id = pk
#         stu = Students.objects.get(pk=id)

#         stu.delete()
#         return Response({'msg':'Data deleted!!'})


# general view and mixins
# class LCStudent(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, *kwargs)

    
# class RUDStudentRetrive(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, *kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, *kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, *kwargs)


# class StudentListCreate(ListCreateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializers

# class StudentRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializers


# class StudentViewSets(viewsets.ViewSet):
#     def list(self, request):
#         stu = Students.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = Students.objects.get(id=id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data)
        
#     def create(self, request):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data created'})
#         return Response(serializer.errors)
    
#     def update(self,request, pk=None):
#         id = pk
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"data updated"})
#         return Response(serializer.errors)
    
#     def partial_update(self, request, pk=None):
#         id = pk
#         stu = Students.objects.get(pk=id)
#         serializer = StudentSerializers(stu , data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"partial data updated"})
#         return Response(serializer.errors)
    
#     def destroy(self, request, pk=None):
#         id = pk
#         stu = Students.objects.get(pk=id)
        
#         stu.delete()
#         return Response({"msg": "data deleted"})

        
    
class StudentModelViewSets(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers

