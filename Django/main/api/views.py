from django.shortcuts import render
from.models import Students
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


def student_detail(request, pk):
    stu = Students.objects.get(id = pk)
    serializer = StudentSerializers(stu)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')


def student_detail_list(request):

    stu = Students.objects.all()
    serializer = StudentSerializers(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')
 

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

# @api_view(['GET'])
# def hello(request):
#     return Response({'msg':'namaste!!'})

# @api_view(['POST'])
# def hello(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This is POST request'})


@api_view(['GET','POST'])
def hello(request):

    if request.method == 'GET':
        return Response({'msg':'This is GET request'}) 
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is POST request', 'data':request.data})