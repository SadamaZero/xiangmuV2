from django.urls import path
from .views import *

# /teacher/
urlpatterns = [
    path('', teacher_center, name='teacher_index'),
]
