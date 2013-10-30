# This Python file uses the following encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from web.models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from web.swift import *

def handle_uploaded_file(email,f):

    root_path = '/home/admin/ThuSwiftDisk/ThuCloudDisk/static/download/'
    user_path = root_path+email+'/'
    file_path = user_path+str(f)
    print "#####file_path###"+file_path
    with open(file_path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    #swift = Swift('swift.strawberrycode.com','demo','admin','secrete','5000')
    #swift.connect()
    #print swift.put_object_from_file(container = 'test-container',prefix = '',filepath = file_path)
    #return HttpResponseRedirect('/home/files')
@csrf_protect
def uploadhandler(request):
    try:
        file = request.FILES['file']
        handle_uploaded_file(request.user.email,file)
    except:
        print '###some wrong  with upload file###'
    return HttpResponseRedirect('/home/files')

def download_file(request):
    file_name = request.GET['file_name']
    #swift = Swift('swift.strawberrycode.com','demo','admin','secrete','5000')
    #swift.connect()
    #swift.get_object_to_file('test-container',file_name)
    return HttpResponse('True')
@csrf_protect
def delete_file(request):
    file_name = request.GET['file_name']
    #swift = Swift('swift.strawberrycode.com','demo','admin','secrete','5000')
    #swift.connect()
    #swift.delete_object('test-container',file_name)
    root_path = '/home/admin/ThuSwiftDisk/ThuCloudDisk/static/download/'
    user_path = root_path+request.user.email+'/'
    os.remove(user_path+file_name)
    return HttpResponseRedirect('/home/files')