from django.shortcuts import render
from .models import student,studentemail
from .serializers import studentSerializer, studentGetSerializer,studentemailSerializer,studentemailGetSerialzer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

# learn proper use of APIView and gneric view

class studentView(APIView):
    def post(self,request):
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'Invaild'},status=status.HTTP_400_BAD_REQUEST)


class studentGetView(APIView):
    def get(self, request):
        stu = student.objects.all()
        sub = []
        # remove loop
        for i in stu:
            serializer = studentGetSerializer(i)
            sub.append(serializer.data)    
        return Response(sub, status=status.HTTP_200_OK)


# add one patch method as well

class studentUpdateView(APIView):
    def put(self,request,id):

        # error handiling missing
        stu=student.objects.get(id=id)
        serializer=studentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated successfully'},status=status.HTTP_200_OK)
        else:
            # error message using serializer
            return Response({'msg':'Invalid'},status=status.HTTP_400_BAD_REQUEST)


class studentDeleteView(APIView):
    def delete(self,request,id):
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Deleted Successfully'},status=status.HTTP_200_OK)

class studentemailView(APIView):
    def post(self,request):
        serializer=studentemailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Saved Successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'Invalid'},status=status.HTTP_400_BAD_REQUEST)

class studentemailGetView(APIView):
    def get(self,request):
        stu=studentemail.objects.all()
        serializer=studentemailGetSerialzer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class studentemailUpdateView(APIView):
    def put(self,request,id):
        stu=studentemail.objects.get(id=id)
        serializer=studentemailSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'msg':'Invalid'},status=status.HTTP_400_BAD_REQUEST)

class studentemailDeleteView(APIView):
    def delete(self,request,id):
        stu=studentemail.objects.get(id=id)
        stu.delete()
        return Response({'Deleted Succesfully'},status=status.HTTP_200_OK)






