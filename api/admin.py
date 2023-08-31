from django.contrib import admin
from .models import StudentDetail
# Register your models here.
@admin.register(StudentDetail)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','age']