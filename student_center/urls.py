from django.urls import path
from .views import *

# /student/
urlpatterns = [
    path('', student_center, name='student_index'),
    path('list', thesis_list, name='thesis_list'),
]
