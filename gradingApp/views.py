from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import simplejson
from random import randint
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from models import *
from django.core.mail import EmailMessage

# Create your views here.
nameDict = {
'viva1': 'Viva -1','midsemPresentation' : 'Mid Semester Presentation','viva2': 'Viva-2','finalDissertation': 'Final Dissertation','finalViva' : 'Final Viva','Total' : 'Total','midsemReport' : 'mid Semester Written Report','midsemGrade': 'Mid Semester Grade','endsemGrade':' End Semester Grade','workProgress':	'Work Progress And Achievement','technicalCompetence' :'Technical/Professional Competence','documentation':'Documentation/Expression','initiative' :'Initiative and Originality','puntuality':'Puntuality','reliability' :'Reliability', 'endDevelopmentReport ': 'Development Related Report', 'endDevelopmentPresentation' :' Development Related Presentation', 'endResearchReport':'Research Related Report', 'endResearchPresentation':'Research Related Presentation', 'midProposalContent': 'Research Proposal Content', 'midProposalPresentation': 'Research Proposal Presentation','midDevelopmentReport': 'Development Related Report','midDevelopmentPresentation' :' Development Related Presentation', 'midResearchReport':'Research Related Report','midResearchPresentation' : 'Research Related Presentation','midsemTotal':'Mid Sem Total','endsemTotal':'End Sem Total','finalThesis':'Final Thesis Report','seminarGrade':'Final Seminar Grade','writtenAbstract':'Written Abstract','technicalContent':'Technical Contents','depthKnowledge':'Depth Of Knowledge','stylePresentation':'Style Of Presentation','responseQuestion':'Response To Questions','midregularityMentor':'Regularity in Interaction with mentor','projectViva1':'Project Viva 1', 'projectViva2' : 'Project Viva 2', 'weekdocumentSubmission' : 'Weekly Report/document Submission','midsemViva': 'MidSem Viva', 'endregularityMentor': 'Regularity in Interaction with mentor','projectViva34':'Project Viva III/IV','finalSeminar': 'Final Seminar','finaldocumentSubmission':'Final report/document submission'}
allow_dict = {'key1':[1,2,3,4],'key2':[2,3,4],'key3':[0,4],'key4':[1,4],'key5':[3,4]}
def AccessPermission(dictkey,val):
	if not val in allow_dict[dictkey]:
		return False
	return True
def index(request):
	return render(request,'blank.html',{'category':int(str(request.session["category"]))})#

# @permission_required('AccessPermission.is_allowed',str(request.session["userid"]),int(str(request.session["category"])))
def dissertation(request):
	if not AccessPermission('key1',int(str(1))):
		raise Http404
	if request.is_ajax():
		print "@@#@!##%$#%"
		data = request.GET.get("x")
		typeTable= request.GET.get("type")   #table1 && table2
		data = ['OK',data+typeTable]
		return HttpResponse(simplejson.dumps(data), content_type='application/json')
	else:
		#ID,Name,token_ID,Eval_Data,Semester,Year,CourseCode,CourseName,
		return render(request,'dissertation.html',{'category':1})#int(str(request.session["category"]))

def researchPractice(request):
	if not AccessPermission('key1',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
		data = request.GET.get("x")
		typeTable= request.GET.get("type")   #table1 && table2
		data = ['OK',data+typeTable]
		return HttpResponse(simplejson.dumps(data), content_type='application/json')
	else:
		#ID,Name,token_ID,Eval_Data,Semester,Year,CourseCode,CourseName,
		return render(request,'ResearchPractice.html',{'category':int(str(request.session["category"]))})#int(str(request.session["category"]))

def thesis(request):
	if not AccessPermission('key1',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
		try:
			data = request.GET.get("x")
			typeTable = request.GET.get("type")
			pk = request.GET.get("pk")
			#get data with pk
			#convert the data from string to dictionary{'Thesis Evaluation':{},'Seminar 1':{},Seminar 2':{},Seminar 3:{},Seminar 4':{},'Traits Evaluation':{}}
			if typeTable =="1":
				pass
				#save table1 data
			elif typeTable =="2":
				sNO = str(request.GET.get("seminar")).strip()
				seminarName = "Seminar" + sNO[-1]
				#save seminar data
			elif typeTable =="3":
				pass
				#save table3 data
			data = ["OK",data]
			
		except:
			data = ["NOK"]
		return HttpResponse(simplejson.dumps(data), content_type='application/json')
	return render(request,'thesis.html',{'category':int(str(request.session["category"]))})#int(str(request.session["category"]))

def projects(request):
	if AccessPermission('key1',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
		try:
			data = request.GET.get("x")
			typeTable = request.GET.get("type")
			pk = request.GET.get("pk")
			# get record
			# convert to dictionary named x
			# x[typeTable] = data
			z = ["OK",data]
		except:
			z = ["NOK"]
		return HttpResponse(simplejson.dumps(z), content_type='application/json')
	return render(request,'Projects.html',{'category':int(str(request.session["category"]))})#int(str(request.session["category"]))

def student(request):
#	data = simplejson.loads(markList.objects.get(student = student.objects.get(userid=str(request.session["userid"]))).evalData)
	table1 = {'midsemTotal':100,'endsemGrade':'A'}
	table2= {'reliability':'A','initiative':'Good'}
	data = {'Mid Sem Evaluation':table1,'End Sem Evaluation':table2}
	for key in data:
		x = data[key]
		print x 
		for key2 in x:
			x[nameDict[key2]] = x.pop(key2)
	context = {'data':data,'bitsid':'2012C6PS392P','name':'prateek jain','category':int(str(request.session["category"]))}
	return render(request,'student.html',context)

def reportDisp(request):
	if not AccessPermission('key3',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
		comment = request.GET.get("comment")
		idx = request.GET.get("id")
		data = ["OK",comment]
		return HttpResponse(simplejson.dumps(data),content_type='application/json')
	else:
		raise Http404

def reportGen(request):
	if not AccessPermission('key1',int(str(request.session["category"]))):
		raise Http404
	return render(request,'genReport.html',{'type':str(request.GET.get('type')),'category':int(str(request.session["category"]))})

def reminder(request):
	if not AccessPermission('key2',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
		try:
			to = str(request.GET.get("to"))
			tolst = to.split(',')
			sub = str(request.GET.get("sub"))
			msg = str(request.GET.get("msg"))
			for i in tolst:
				x = reminder_details(userid=userData.objects.get(userid=str(request.session["userid"])),reciever = i,subject = sub,message = msg)
				x.save()
			email = EmailMessage(sub,msg,to=tolst)
			email.send()
			data = ["OK"]
		except Exception,e:
			print e
			data = ["NOK"]
		return HttpResponse(simplejson.dumps(data),content_type='application/json')
	return render(request,'reminder.html',{'category':int(str(request.session["category"]))})

def midSemReport(request):
	if not AccessPermission('key4',int(str(request.session["category"]))):
		raise Http404
	if request.method=='POST':
		token = False
		print request.GET.get('type')
		print request.GET.get('id')
		if request.FILES:
			return redirect('/grade/midSemReport?token=1')
		else:
			return redirect('/grade/midSemReport?token=0')
	else:
		token = request.GET.get('token',None)
		if token:
			return render(request,'midSemReport.html',{'token':token})
		else:	
			return render(request,'midSemReport.html',{'category':int(str(request.session["category"]))})

def courses(request):
	if not AccessPermission('key5',int(str(request.session["category"]))):
		raise Http404
	if request.is_ajax():
#		print "@$##@%@%^#%&^%^#$%@%@%^#%$"
		action = int(request.GET.get("action"))
		npk = randint(2,9)
		try:
			if action==0:
				#save new data
				code = str(request.GET.get("code"))
				courseTitle = str(request.GET.get("title"))
				print courseTitle
				x = course(courseCode = code,title=courseTitle)
				x.save()
				npk = course.objects.get(courseCode=code).pk
			elif action ==1:
				#update data
				code = str(request.GET.get("code"))
				courseTitle = str(request.GET.get("title"))
				pk = str(request.GET.get("pk"))
				x = course.objects.get(pk=pk)
				x.courseCode = code
				x.title = courseTitle
				x.save()
				npk = pk
			elif action==2:
				pk = str(request.GET.get("pk"))
				#delete data
				x = course.objects.get(pk=pk)
				x.delete()
				npk = pk
			data = ["OK",npk]
		except Exception,e:
			print e
			data = ["NOK"]
		return HttpResponse(simplejson.dumps(data),content_type='application/json')
	else:
		x = course.objects.all()
		# lst = [[1,'CS12','asd'],[2,'CS21','dsfds'],[3,'CS34','nhghg'],[4,'CS99','cxxc'],[5,'CS31','rdsf']]
		lst = []
		for z in x:
			lst1 =[z.pk,z.courseCode,z.title]
			lst.append(lst1)
		return render(request,'courses.html',{'courseData':lst,'category':int(str(request.session["category"]))})