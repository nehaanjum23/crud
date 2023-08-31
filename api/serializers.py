from rest_framework import serializers
from .models import student,studentemail

class studentSerializer(serializers.ModelSerializer):

    # no need to define fields here
    name = serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    class Meta:
        model=student
        fields=['name','roll','city']  # list and tuple 


class studentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

class studentemailSerializer(serializers.ModelSerializer):
    # no need to define fields here

    name=serializers.CharField(max_length=256)
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=studentemail
        fields=['name','email']

class studentemailGetSerialzer(serializers.ModelSerializer):
    class Meta:
        model=studentemail
        fields='__all__'
