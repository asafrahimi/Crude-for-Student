from django.conf.urls import include, url
from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from . import views
#from .views import IdList
from .views import StudentsView, StudentView
from .views import StudentsGradesView, StudentGradeView

urlpatterns = [
    #url(r'^$', views.index_student, name='index_student'),
    path('students/', StudentsView),
    path('student/<int:nm>/', StudentView),

    path('studentsgrades/', StudentsGradesView),
    path('studentgrade/<int:nm>', StudentGradeView),
]
