from django.shortcuts import render
from django.http import Http404,HttpResponse
import simplejson
from models import *
from django.contrib.auth.decorators import login_required

allow_dict = {'key1':[1,2,3,4],'key2':[2,3,4],'key3':[0,4],'key4':[1,4],'key5':[3,4]}
def AccessPermission(dictkey,val):
	if not val in allow_dict[dictkey]:
		return False
	return True
@login_required(login_url='/')
def onOff(request):
	if request.is_ajax():
		try:
			appID = request.GET.get("appID")
			print appID
			print request.GET.get("start")
			print request.GET.get("end")
			start = request.GET.get("start")
			end = request.GET.get("end")
			data = ["NOK"]
			if end > start:
				print "hello"
				data = ["OK"]
				x = appName.objects.get(appID=appID)
				y = appOnOff(app=x,startDate=start,endDate=end)
				y.save()
		except Exception,e:
			print e
			data = ["NOK"]
		return HttpResponse(simplejson.dumps(data),content_type='application/json')
	z = appName.objects.filter()
	lst=[]
	
	for item in z:
		y = appOnOff.objects.filter(app=item)
		aid=item.appID
		name=item.appName
		if not y.count()==0:
			y=y.order_by('-pk')
			y=y[0]
			startd=y.startDate
			endd=y.endDate
		else:
			startd=''
			endd=''
		templist=[aid,name,startd,endd]
		print templist
		lst.append(templist)
	#lst = [[appName.appID.get,'oct','2/12/2015',''],[1,'onct','2/12/2015',''],[2,'grading','2/12/2015',''],[3,'electives','2/12/2015','']]
	data = {'AppData':lst,'count':len(lst),'category':int(str(request.session["category"]))}
	return render(request,'appOnOff.html',data)
