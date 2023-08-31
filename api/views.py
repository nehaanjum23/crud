from .models import student
from .serializers import studentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.

# learn proper use of APIView and gneric view

class StudentView(GenericAPIView, ListModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs )

class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs )
    

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs )


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs )


class StudentUpdate(GenericAPIView, DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs )



    


