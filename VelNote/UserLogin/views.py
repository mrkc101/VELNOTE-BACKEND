from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication , SessionAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token= Token.objects.create(user=user)

            return Response({'token': token.key , 'user':serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response (serializer.data)
            