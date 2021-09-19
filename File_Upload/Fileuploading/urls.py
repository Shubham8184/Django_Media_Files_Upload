from django.urls import path
from .views import *


urlpatterns=[
    path('file/',Fileupload,name='file'),
    path('newfile/',model_form_upload,name='newfile'),
    path('showfile/',showfileview,name='showfile'),
    path('home/',Homeview,name='home')
]