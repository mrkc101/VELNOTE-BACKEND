from rest_framework import serializers
from .models import Notes

class Noteserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notes
        fields =  ['id','title','content','created_at','updated_at','file']
