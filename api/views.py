from .models import StudentDetail
from rest_framework.response import Response
from rest_framework.views import APIView

class StudentView(APIView):
    def post(self,request):

        data = request.data 

        if 'first_name' in data and 'last_name' in data and 'age' in data: # NOTE
            student = StudentDetail(first_name=data['first_name'], last_name=data['last_name'], age=data['age'])
            student.save()
            return Response({'message': 'Student created successfully'})
        else:
            return Response({'error': 'Missing required fields'}, status=400)


class StudentGetView(APIView): #as told done without loop
     def get(self, request):
        students = StudentDetail.objects.values('first_name', 'last_name', 'age')
        return Response(list(students))
#     def get(self, request):
#         students = StudentDetail.objects.all()
#         student_data = [
            
#             {'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age}
#             for student in students
#         ]
#         # NOTE: Try to do it without loop
#         return Response(student_data)


class StudentUpdateView(APIView):
    def put(self, request, id):
        data = request.data

        try:
            student = StudentDetail.objects.get(id=id)

            if 'first_name' in data:
                student.first_name = data['first_name']
            if 'last_name' in data:
                student.last_name = data['last_name']
            if 'age' in data:
                student.age = data['age']

            student.save()
            return Response({'message': 'Student updated successfully'})
        except StudentDetail.DoesNotExist:
            return Response({'error': 'Student not found'})


class StudentDeleteView(APIView):
    def delete(self, request, id):
        try:
            student = StudentDetail.objects.get(id=id)
            student.delete()
            return Response({'message': 'Student deleted successfully'})
        except StudentDetail.DoesNotExist:
            return Response({'error': 'Student not found'})