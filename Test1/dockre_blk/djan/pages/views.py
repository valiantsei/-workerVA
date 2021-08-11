import os
from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.http import HttpResponse


def homePageView(request):
#    if not os.path.exists('/usr//ipTmp'):
#        with open('/tmp/in/ipTmp','w') as f:
#            f.write('1.1.1.1/32\n')
#    else:
    with open('/usr/share/ipTmp','a+') as f:
         f.write('1.1.1.1/32\n')
    return HttpResponse('Hello, World! bbbb')
