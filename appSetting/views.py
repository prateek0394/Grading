from django.shortcuts import render
from django.http import Http404,HttpResponse
import simplejson

allow_dict = {'key1':[1,2,3,4],'key2':[2,3,4],'key3':[0,4],'key4':[1,4],'key5':[3,4]}
def AccessPermission(dictkey,val):
	if not val in allow_dict[dictkey]:
		return False
	return True

def onOff(request):
	if not AccessPermission('key5',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
		try:
			appID = request.GET.get("appID")
			print appID
			print request.GET.get("start")
			print request.GET.get("end")
			data = ["OK"]
		except:
			data = ["NOK"]
		return HttpResponse(simplejson.dumps(data),content_type='application/json')
	lst = [[0,'oct','2/12/2015',''],[1,'onct','2/12/2015',''],[2,'grading','2/12/2015',''],[3,'electives','2/12/2015','']]
	data = {'AppData':lst,'count':len(lst),'category':int(str(request.session["category"]))}
	return render(request,'appOnOff.html',data)
