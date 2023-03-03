from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout
from .models import User
from . import serializers
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def Register(request):
    data = request.data
    email = data.get('email',None)
    if User.objects.filter(email=email).exists():
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
    serializer = serializers.RegisterSerializers(data = request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def Login(request):
    data = request.data
    email = data.get("email",None)
    password = data.get("password",None)

    try:
        user = authenticate(email=email,password=password)
    except:
        return Response("email or password is wrong")
    if user:
        login(request, user)    
        print(request.user)
        request.session['user'] = user.id
        print( request.session['user'])
        return Response({"usersession":request.session['user'],"status":status.HTTP_200_OK})
    return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

@api_view(['POST'])
def Logout(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def admin_login(request):
    email = request.data.get('email',None)
    password = request.data.get('password',None)
    print(email)
    admin = authenticate(request,email=email, password=password)
    if admin is not None:
        login(request, admin)
        request.session['admin'] = admin.id
        return Response({"usersession":request.session['user'],"status":status.HTTP_200_OK})
    else:
      print("error")
    return Response("logedin")