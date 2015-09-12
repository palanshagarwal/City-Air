from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.template.response import TemplateResponse

import urllib
import urllib2
#from urllib2 import Request, urlopen, URLError
import StringIO, json

breeze_key='82b31539844a4a5b8fc2dbd9f1fd232d'
          
@login_required  
def ip_to_latlong(request):
    global breeze_key
    master={}
    lat = '' #'40.7324296'
    lng =  '' #'-73.9977264'
    url = 'http://ipinfo.io/json'
    j = urllib2.urlopen(url)
    j_obj = json.load(j)
    j.close()
    for k,v in j_obj.items():
        if k=='loc':
            stri = v.split(',')
            lat = stri[0]
            lng = stri[1]
    data_url = 'http://api-beta.breezometer.com/baqi/?lat='+lat+'&lon='+lng+'&key='+breeze_key
    j = urllib2.urlopen(data_url)
    j_obj = json.load(j)
    j.close()
    #return HttpResponse(j_obj.items())
    for k,v in j_obj.items():
        master[k]=v

    response=render_to_response('temp.html', {"values": master})
    return response
#
#