from django.shortcuts import render,redirect
from .forms import DocumentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Document
from django.contrib import messages
from django.contrib.auth.models import User


def Fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'Fileupload/fileupload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'Fileupload/fileupload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'File is uploaded Successfullyy!!!...')
            return redirect('newfile')
    else:
        form = DocumentForm()
    return render(request, 'Fileupload/newfileupload.html', {
        'form': form
    })


def showfileview(request):
    file=Document.objects.all()
    template_name='Fileupload/showfile.html'
    context={'file':file}
    return render(request,template_name,context)


def Homeview(request):
    template_name='Fileupload/home.html'
    return render(request,template_name)

