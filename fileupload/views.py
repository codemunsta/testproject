from django.shortcuts import render
from django.views.generic import TemplateView
from .document import school_fees_check
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


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

# Create your views here.
