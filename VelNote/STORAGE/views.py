from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view ,  permission_classes
from .models import Notes
from .serializers import Noteserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

def index(request):
    return HttpResponse("hello world")

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def notes(request):
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = Noteserializer(notes,many=True)
    
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    

    if request.method == 'POST':
        serializer = Noteserializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)