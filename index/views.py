from django.shortcuts import render
# from upload_file.models import UserFile
# from bulletin.models import Bulletin


def index(request):
    context = {}
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
