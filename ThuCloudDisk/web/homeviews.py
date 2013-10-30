# This Python file uses the following encoding: utf-8
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from web.models import MyUser
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from web.swift import *
import json
import datetime

@login_required(login_url='/login')
@csrf_protect
def files(request):
    user = request.user
    #swift = Swift('swift.strawberrycode.com','demo','admin','secrete','5000')
    #swift.connect()
    #tuple =  swift.list_container('test-container');
    #file_list = []
    #for f in tuple[1]:
    #    file_list.append({'name':f['name'],'last_modified':f['last_modified'],'bytes':f['bytes']})
    #print file_list
    #container = Container(root_xml)
    #print container.list()
    root_path = '/home/admin/ThuSwiftDisk/ThuCloudDisk/static/download/'
    user_path = root_path+user.email+'/'
    files = os.listdir(user_path)
    file_list=[]
    for f in files:
        file_list.append({'name':f,'bytes':os.path.getsize(user_path+f),'last_modified':datetime.datetime.fromtimestamp(os.path.getmtime(user_path+f))})
    #print file_list
    return render(request,'home/files.html',locals())