from django.contrib import admin
from .models import Student, StudentGrade

#admin.site.register([Id])
admin.site.register(Student)
admin.site.register(StudentGrade)
# Register your models here.
