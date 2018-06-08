from django.shortcuts import render
from rbac.views import permission


@permission
def student_center(request, *args, **kwargs):
    action_list = kwargs.get('action_list')
    menu_string = kwargs.get('menu_string')
    username = request.session['user_info']['username']
    context = {}
    context['username'] = username
    response = render(request, 'student_center/student_center.html', context)
    response.set_cookie('role', 'student')
    return response


def thesis_list(request):
    username = request.session['user_info']['username']
    context = {}
    context['username'] = username
    return render(request, 'student_center/thesis_list.html', context)
