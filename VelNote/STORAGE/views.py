from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view ,  permission_classes
from .models import Notes
from .serializers import Noteserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


def index(request):
    return HttpResponse("hello world")


class NoteAPI(APIView):
    permission_classes = [IsAuthenticated]  
    
    def put(self, request, pk=None):
        print(f"Received pk: {pk}")  # Debugging output
        try:
            note = Notes.objects.get(id=pk)
        except Notes.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Noteserializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = Noteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is not None:
            try:
                note = Notes.objects.get(id=pk)
                serializer = Noteserializer(note)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Notes.DoesNotExist:
                return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # If pk is None, return all notes
        notes = Notes.objects.all()
        serializer = Noteserializer(notes, many=True)
        return Response({'UPLOADS':serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, pk=None):
        try:
            note = Notes.objects.get(id=pk)
        except Notes.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Noteserializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk = None):
        note = Notes.objects.get(id=pk)
        note.delete()
        return Response (status=status.HTTP_200_OK)


























# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def notes(request):
#     if request.method == 'GET':
#         notes = Notes.objects.all()
#         serializer = Noteserializer(notes,many=True)
    
#         return Response(serializer.data,status=status.HTTP_302_FOUND)
    

#     if request.method == 'POST':
#         serializer = Noteserializer(data=request.data,many=True)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)