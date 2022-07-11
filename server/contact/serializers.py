from dataclasses import fields
from pyexpat import model
from .models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
      class Meta:
            model = Contact
            fields = '__all__'
            
            