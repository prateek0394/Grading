from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.views.generic.base import View
from social_auth.exceptions import AuthFailed
from social_auth.views import complete
from django.shortcuts import render,redirect
from models import userData,logForUsers,uploadDelete
import time
def home(request):
    if not request.user.is_anonymous():
        print "#@#@#@$#@"
        tempUser =  str(request.user)
        isUser = userData.objects.filter(userid=tempUser).count()
        if not isUser==0:
            User = userData.objects.get(userid=tempUser)
            request.session["userid"] = tempUser
            request.session["category"] = User.userType
            vr = logForUsers(user = User)
            vr.save()
            return redirect('/grade/')
        return HttpResponse("<h1>Not A Valid User.</h1><br><a href = '/exit/'>logout</a>")
    context = {'request':request,'user': request.user}
    return render(request,'home.html',context)
 
def logout(request):
    return redirect('https://mail.google.com/?logout')

def insertData(f,idu):
    if idu=="Student":
        idu = 0
    elif idu=="Faculty":
        idu = 1
    elif idu =="Staff":
        idu = 2
    elif idu =="All":
        idu = -1
    for i in f:
        lst = i.split(';')
        if idu > -1:
            x = userData(userid=lst[0],bitsid=lst[1],name=lst[2],userType=idu)
        else:
            x = userData(userid=lst[0],bitsid=lst[1],name=lst[2],userType=lst[3])
        x.save()

def deleteData(f):
    for i in f:
        try:
            z = str(i)
            x = userData.objects.get(userid=z)
            x.delete
        except:
            pass

def upload(request):
    if str(request.session["userid"])=="cs.elective":
        if request.method=="POST":
            try:
                fil = request.FILES["dataFile"]
                operation = request.POST.get("oper")
                usertype = request.POST.get("userType")
                x = uploadDelete(operation=operation,uploadFile=fil)
                x.save()
                f = open('userData/'+ x.operation+'/'+fil.name,'r+')
                if operation =="Data Insertion":
                    insertData(f,usertype)
                else:
                    deletData(f)
                return render(request,'dataUpload.html',{'status':1,'msg':'OK','category':int(request.session["category"])})
            except Exception,e:
                print e
                return render(request,'dataUpload.html',{'status':-1,'msg':str(e),'category':int(request.session["category"])})
        else:
            return render(request,'dataUpload.html',{'status':0,'msg':'start','category':int(request.session["category"])})
    else:
        raise Http404

"""class AuthComplete(View):
    def get(self, request, *args, **kwargs):
        backend = kwargs.pop('backend')

        try:
            return complete(request, backend, *args, **kwargs)
        except AuthFailed:
            messages.error(request, "Your Google Apps domain isn't authorized for this app")
            return HttpResponseRedirect(reverse('login'))
 
 
class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)"""