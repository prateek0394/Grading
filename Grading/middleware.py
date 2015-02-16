import datetime
from django.conf import settings
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import redirect
from appSetting.models import *
def checkGrade(request, x):
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
    
def checkSetting(request, x):
    if x[1] =="OnOff" and not int(request.session["category"])==3 and not int(request.session["category"]==4):
        raise Http404

class StayMiddleware(object):
    def process_request(self,request):
        x = str(request.path)
        x = x.split('/')[1:]
        # print x
        if not request.user.is_anonymous():
            if x[0] =="grade":
                xy = appOnOff.objects.filter(app = appName.objects.get(appID  = 4)).order_by("-pk")[0]
                if xy.startDate == "" or xy.endDate == "":
                    return HttpResponse("Application not properly configured!!! Contact Administrator for that")
                elif datetime.strptime(xy.startDate,"%m/%d/%Y") > datetime.now() or datetime.strptime(xy.endDate,"%m/%d/%Y") < datetime.now():
                    raise Http404
                else:
                    return checkGrade(request, x)
            elif x[0] == "appSetting":
                    return checkSetting(request, x)