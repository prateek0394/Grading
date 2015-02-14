import datetime
from django.conf import settings
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import redirect

def checkGrade(x):
    if x[1] =="student":
        if not (int(request.session["category"]) ==0 or int(request.session["category"]) == 4):
            raise Http404
    elif x[1] =="reportDisp":
        if not (int(request.session["category"]) == 0 or int(request.session["category"]) == 4):
            raise Http404
    elif x[1] =="submitReport":
        if int(request.session["category"]) == 0 :
            raise Http404
    elif x[1] =="courses":
        if not (int(request.session["category"]) ==3 or int(request.session["category"]) == 4):
            raise Http404
    elif x[1] =="reportGen":
        if int(request.session["category"])==0:
            raise Http404
    elif x[1] =="reminder":
        if int(request.session["category"]) == 0 or int(request.session["category"]) == 1:
            raise Http404
    elif x[1] =="marks":
        if int(request.session["category"])==0:
            raise Http404
    
def checkSetting(x):
    if x[1] =="OnOff" and not(int(request.session["category"])==3 and int(request.session["category"]==4)):
        raise Http404

class StayMiddleware(object):
    def process_request(self,request):
        x = str(request.path)
        x = x.split('/')[1:]
        print x
        if not request.user.is_anonymous():
            print "dsadsd"
            if x[0] =="grade":
                return checkGrade(x)