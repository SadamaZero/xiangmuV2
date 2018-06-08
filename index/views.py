from django.shortcuts import render
# from upload_file.models import UserFile
# from bulletin.models import Bulletin


def index(request):
    context = {}

    # index 登陆状态，不同内容
    if 'role' in request.COOKIES:  # center视图函数设置的role cookie
        if request.COOKIES['role'] == 'student':
            context['login_state'] = 'student'
        elif request.COOKIES['role'] == 'teacher':
            context['teacher'] = 'teacher'
    else:
        context['login_state'] = False
    # files = show_files()
    # context['files'] = files

    # bulletins = show_bulletins()
    # context['bulletins'] = bulletins
    return render(request, 'index.html', context)


# def show_files():
#     files = UserFile.objects.all()
#     return files
#
#
# def show_bulletins():
#     bulletins = Bulletin.objects.all()
#     return bulletins
