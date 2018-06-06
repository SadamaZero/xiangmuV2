from django.shortcuts import render
from rbac.views import permission


def student_center(request):
    username = request.session['user_info']['username']
    context = {}
    context['username'] = username
    return render(request, 'student_center/student_center.html', context)


def thesis_list(request):
    username = request.session['user_info']['username']
    context = {}
    context['username'] = username
    return render(request, 'student_center/thesis_list.html', context)
