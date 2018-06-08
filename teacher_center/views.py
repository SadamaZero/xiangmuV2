from django.shortcuts import render
from rbac.views import permission


@permission
def teacher_center(request, *args, **kwargs):
    action_list = kwargs.get('action_list')
    menu_string = kwargs.get('menu_string')
    username = request.session['user_info']['username']
    context = {}
    context['username'] = username
    response = render(request, 'teacher_center/teacher_center.html')
    response.set_cookie('role', 'teacher')
    return response
