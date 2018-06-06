from django.shortcuts import render


def teacher_center(request):
    return render(request, 'teacher_center/teacher_center.html')
