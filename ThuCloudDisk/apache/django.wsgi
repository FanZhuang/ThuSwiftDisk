#-*-coding:utf-8-*-
import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE']='ThuCloudDisk.settings'
app_apth='/home/admin/ThuSwiftDisk/ThuCloudDisk'
sys.path.append(app_apth)
application=django.core.handlers.wsgi.WSGIHandler()

