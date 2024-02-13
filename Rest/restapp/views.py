from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
# from restapp. models import Person
from .serializer import *
from rest_framework import status


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data =  data)  #validation

        if not serializer.is_valid():  # Serializer is not valid => false
            return Response({
                'status':False,
                'message': serializer.errors
                },status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'status':True, 'message':'user created'},status.HTTP_201_CREATED)
            
class loginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = Loginserializers(data = data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        
        print(serializer.data)
        user = authenticate(username = serializer.data['username'],password = serializer.data['password'])
        print(user)
        if not user:
             return Response({
                'status':False,
                'message':'invalid credentials'
            },status.HTTP_400_BAD_REQUEST)


        token, _ = Token.objects.get_or_create(user=user)
        print(token)
        return Response({'status':True, 'message':'user Login created','token': str(token)},status.HTTP_201_CREATED)

    

class PersonAPI(APIView):
    def get(self,request):
        objs = Person.objects.all()
        serializer = PersonSerializer(objs,many = True)
        return Response(serializer.data)
    
       
    
    def post(self,request):
        data = request.data
        serializer= PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'] )
        serializer = PersonSerializer(obj,data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'person deleted'})


@api_view(['GET','POST','PUT'])
def index(request):
    couses ={
            'course_name':'python',
            'learn':['flask','rest_api','fast_api','bottle'],
            'course_provider':'scalar'
        }
    
    if request.method == 'GET':
        print('YOU ARE HITTIN GET METHOD')
        return Response(couses)
        
    
    elif request.method == 'POST':
        data = request.data
        print('********')
        print(data)
        print('************')

        print('YOU ARE HITTING POST METHOD!!!')
        return Response(couses)
    
    elif request.method == 'PUT':
        print('YOU ARE HITTING PUT METHOD!!!')
        return Response(couses)
    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PersonSerializer(objs,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer= PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'] )
        serializer = PersonSerializer(obj,data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'person deleted'})


    
    


