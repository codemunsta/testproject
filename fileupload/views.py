from django.shortcuts import render
from django.views.generic import TemplateView
from .document import school_fees_check
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib import messages
from .models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    if request.method == 'POST':
        names = request.POST['name']
        uploaded_file = request.FILES['document']
        filestorage = FileSystemStorage()
        name = filestorage.save(uploaded_file.name, uploaded_file)
        check = school_fees_check(filestorage.path(name), mat_no='PSC1808972', session='2020/2021')
        if check == 0:
            messages.success(request, f'{names} your document is accepted')
            return render(request, 'upload.html')
        else:
            messages.error(request, f'{names} {check}')
            return render(request, 'upload.html')
    else:
        return render(request, 'upload.html')


@api_view(['POST'])
def Login(request):

    username = request.POST["email"]
    password = request.POST["password"]

    check_user = User.objects.filter(username=username).exists()
    if check_user is False:
        msg = {"status": False, "message": "User with the email does not exists."}
        return JsonResponse(msg)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        data = {
            'token': 'token',
            'username': username,
            'msg': {
                'status': True,
                'message': 'successfully logged in'
            }
        }
        return Response(data)
    else:
        msg = {"status": False, "message": "Invalid Email/Password."}
        return Response(msg)


# Create your views here.
