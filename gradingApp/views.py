from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import simplejson
from random import randint
# from django.contrib.auth.decorators import permission_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from models import *
from finalauth.models import *
from django.core.mail import EmailMessage
import datetime
nameDict = {
'viva1': 'Viva -1','midsemPresentation' : 'Mid Semester Presentation','viva2': 'Viva-2','finalDissertation': 'Final Dissertation','finalViva' : 'Final Viva','Total' : 'Total','midsemReport' : 'mid Semester Written Report','midsemGrade': 'Mid Semester Grade','endsemGrade':' End Semester Grade','workProgress':	'Work Progress And Achievement','technicalCompetence' :'Technical/Professional Competence','documentation':'Documentation/Expression','initiative' :'Initiative and Originality','puntuality':'Puntuality','reliability' :'Reliability', 'endDevelopmentReport': 'Development Related Report', 'endDevelopmentPresentation' :'Development Related Presentation', 'endResearchReport':'Research Related Report', 'endResearchPresentation':'Research Related Presentation', 'midProposalContent': 'Research Proposal Content', 'midProposalPresentation': 'Research Proposal Presentation','midDevelopmentReport': 'Development Related Report','midDevelopmentPresentation' :' Development Related Presentation', 'midResearchReport':'Research Related Report','midResearchPresentation' : 'Research Related Presentation','midsemTotal':'Mid Sem Total','endsemTotal':'End Sem Total','finalThesis':'Final Thesis Report','seminarGrade':'Final Seminar Grade','writtenAbstract':'Written Abstract','technicalContent':'Technical Contents','depthKnowledge':'Depth Of Knowledge','stylePresentation':'Style Of Presentation','responseQuestion':'Response To Questions','midregularityMentor':'Regularity in Interaction with mentor','projectViva1':'Project Viva 1', 'projectViva2' : 'Project Viva 2', 'weekdocumentSubmission' : 'Weekly Report/document Submission','midsemViva': 'MidSem Viva', 'endregularityMentor': 'Regularity in Interaction with mentor','projectViva34':'Project Viva III/IV','finalSeminar': 'Final Seminar','finaldocumentSubmission':'Final report/document submission'}
# allow_dict = {'key1':[1,2,3,4],'key2':[2,3,4],'key3':[0,4],'key4':[1,4],'key5':[3,4]}
now = datetime.datetime.now()
month = now.month
year = now.year
semester = 1
if month < 7:
	semester = 2
durObj  = duration.objects.get(semester = semester,year = year)

# def AccessPermission(dictkey,val):
# 	if not val in allow_dict[dictkey]:
# 		return False
# 	return True
@login_required(login_url='/')
def index(request):
	return render(request,'blank.html',{'category':int(str(request.session["category"]))})#
@login_required(login_url='/')
def marks(request):
	if request.is_ajax():
		try:
			tabname = str(request.GET.get('tabname'));
			enterdata = request.GET.get('data')
			print enterdata
			midsemGrade = request.GET.get('midsemGrade','')
			endsemGrade = request.GET.get('endsemGrade','')
			print endsemGrade
			token = request.GET.get('id')
			ob = markList.objects.get(pk=token)
			ob.midSemGrade = midsemGrade
			ob.endSemGrade = endsemGrade
			z = ob.evalData
			z = simplejson.loads(z)
			z[tabname] = str(enterdata)
			z = simplejson.dumps(z)
			ob.evalData = z
			ob.save()
			data = ["OK"]
		except Exception,e:
			data = ["NOK",str(e)]
		return HttpResponse(simplejson.dumps(data), content_type='application/json')
	context = {'semester':durObj.semester,'year':durObj.year,'data':{},'category':int(request.session["category"]),'gradeList':["","A","A-","B","B-","C","C-","D","E","NC"],'seminarList':["Good","Poor"],'seml':[7,8,9,10],'trait':["Excellent","Good","Fair","Poor"]}
	try:
		uid = str(request.session["userid"])
		x = userData.objects.get(userid = uid)
		# data = {'semester':,'year':,'faculty':}
		if str(request.session["userid"]) =="1":
			m = markList.objects.filter(faculty=x,dur = durObj).order_by('course')
		else:
			m = markList.objects.filter(dur = durObj).order_by('faculty','course')
		lst = []
		ct = courseTemplates.objects.all()
		courTemp = {}
		for t in ct:
			courTemp[str(t.courseN.courseCode)] = int(t.keyDev)
			#print t.courseN.courseCode,t.keyDev
		facultylst = list(set([nb.faculty.user.userid for nb in m]))
		# print '$@#%@$#%@^%^%'
		print facultylst
		dataLst = {}
		for we in facultylst:
			perLst = {}
			sublist = ""
			for ze in m:
				if we == ze.faculty.user.userid:
					perLst["name"] = str(ze.faculty.user.name)
					if not courTemp[ze.course.courseCode] in perLst:
						perLst[courTemp[ze.course.courseCode]] = []
						sublist = sublist+str(courTemp[ze.course.courseCode])
					stuLst = [ze.pk,ze.student.user.bitsid,ze.student.user.name,ze.course.courseCode,ze.midSemGrade,ze.endSemGrade]
					#print "$@#$@#$@#$@#"
					x =  simplejson.loads(ze.evalData)
					# print x
					for key in x:
						if type(x[key]) is unicode:
							x[key] = simplejson.loads(str(x[key]))
					if courTemp[ze.course.courseCode] == 1:
						if not "MidSemEvaluation" in x:
							x["MidSemEvaluation"] = {}
						if not "EndSemEvaluation" in x:
							x["EndSemEvaluation"]  = {}
						stuLst.append(x["MidSemEvaluation"])
						stuLst.append(x["EndSemEvaluation"])
					elif courTemp[ze.course.courseCode] == 2:
						if not "Evaluation" in x:
							x["Evaluation"] = {}
						if not "StudentTraits" in x:
							x["StudentTraits"] = {}
						stuLst.append(x["Evaluation"])
						stuLst.append(x["StudentTraits"])
					elif courTemp[ze.course.courseCode] ==3:
						if not "MidSemEvaluation" in x:
							x["MidSemEvaluation"] = {}
						if not "EndSemEvaluation"in x:
							x["EndSemEvaluation"] = {}
						stuLst.append(x["MidSemEvaluation"])
						stuLst.append(x["EndSemEvaluation"])
					elif courTemp[ze.course.courseCode] ==4:
						if not "Evaluation" in x:
							x["Evaluation"] = {}
						if not "Seminar1" in x:
							x["Seminar1"] = {}
						if not "Seminar2" in x:
							x["Seminar2"] = {}
						if not "Seminar3" in x:
							x["Seminar3"] = {}
						if not "Seminar4" in x:
							x["Seminar4"] = {}
						if not "StudentTraits" in x:
							x["StudentTraits"] = {}
						stuLst.append(x["Evaluation"])
						stuLst.append(x["Seminar1"])
						stuLst.append(x["Seminar2"])
						stuLst.append(x["Seminar3"])
						stuLst.append(x["Seminar4"])
						stuLst.append(x["StudentTraits"])
					# print 'nex'
					perLst[courTemp[ze.course.courseCode]].append(stuLst)
			perLst['sublist'] = sublist
			dataLst[str(we)] = perLst						
		print dataLst
		context['data'] = dataLst
	except Exception,e:
		print e
	return render(request,'marks.html',context)

# @permission_required('AccessPermission.is_allowed',str(request.session["userid"]),int(str(request.session["category"])))
# def dissertation(request):
# 	if not AccessPermission('key1',int(str(1))):
# 		raise Http404
# 	if request.is_ajax():
# 		print "@@#@!##%$#%"
# 		data = request.GET.get("x")
# 		typeTable= request.GET.get("type")   #table1 && table2
# 		data = ['OK',data+typeTable]
# 		return HttpResponse(simplejson.dumps(data), content_type='application/json')
# 	else:
# 		#ID,Name,token_ID,Eval_Data,Semester,Year,CourseCode,CourseName,
# 		return render(request,'dissertation.html',{'category':1})#int(str(request.session["category"]))

# def researchPractice(request):
# 	if not AccessPermission('key1',4):#int(str(request.session["category"]))):
# 		raise Http404
# 	if request.is_ajax():
# 		data = request.GET.get("x")
# 		typeTable= request.GET.get("type")   #table1 && table2
# 		data = ['OK',data+typeTable]
# 		return HttpResponse(simplejson.dumps(data), content_type='application/json')
# 	else:
# 		'''
# 		Data format = {'MidSemEvaluation':{'midProposalContent':'','midProposalPresentation':'','midDevelopementReport':'','midDevelopmentPresentation':'','midResearchReport':'','midResearchPresentation':'','midsemTotal':''},
# 		'EndSemEvaluation':{'endDevelopmentReport':'','endDevelopmentPresentation':'','endResearchReport':'','endResearchPresentation':'','endsemTotal':'','Total':''}}
# 		'''
# 		#get the present year semester

# 		# cor = course.objects.filter(title = 'Research Practice')
# 		# uid = str(request.session["userid"])
# 		# x  = userData.objects.get(userid = uid)
# 		# lst = []
# 		# if x.userType > 1:
# 		# 	#get all the data
# 		# 	for cx in cor:
# 		# 		stuData = markList.objects.filter(course = cx)
# 		# 		for i in stuData:
# 		# 			data = simplejson.loads(i.evalData)
# 		# 			sd = [i.pk,i.student.bitsid,i.student.name,data]
# 		# 			lst.append(sd)
# 		# else:
# 		# 	for cx in cor:
# 		# 		stuData = markList.objects.filter(course = cx,faculty = x)
# 		# 		for i in stuData:
# 		# 			data = simplejson.loads(i.evalData)
# 		# 			sd = [i.pk,i.student.bitsid,i.student.name,data]
# 		# 			lst.append(sd)
# 		#context = {'Semester':,'Year':}
# 		#ID,Name,token_ID,Eval_Data,Semester,Year,CourseCode,CourseName,
# 		return render(request,'ResearchPractice.html',{'category':4})#int(str(request.session["category"]))})#int(str(request.session["category"]))

# def thesis(request):
# 	if not AccessPermission('key1',int(str(request.session["category"]))):
# 		raise Http404
# 	if request.is_ajax():
# 		try:
# 			data = request.GET.get("x")
# 			typeTable = request.GET.get("type")
# 			pk = request.GET.get("pk")
# 			#get data with pk
# 			#convert the data from string to dictionary{'Thesis Evaluation':{},'Seminar 1':{},Seminar 2':{},Seminar 3:{},Seminar 4':{},'Traits Evaluation':{}}
# 			if typeTable =="1":
# 				pass
# 				#save table1 data
# 			elif typeTable =="2":
# 				sNO = str(request.GET.get("seminar")).strip()
# 				seminarName = "Seminar" + sNO[-1]
# 				#save seminar data
# 			elif typeTable =="3":
# 				pass
# 				#save table3 data
# 			data = ["OK",data]
			
# 		except:
# 			data = ["NOK"]
# 		return HttpResponse(simplejson.dumps(data), content_type='application/json')
# 	return render(request,'thesis.html',{'category':int(str(request.session["category"]))})#int(str(request.session["category"]))

# def projects(request):
# 	if AccessPermission('key1',int(str(request.session["category"]))):
# 		raise Http404
# 	if request.is_ajax():
# 		try:
# 			data = request.GET.get("x")
# 			typeTable = request.GET.get("type")
# 			pk = request.GET.get("pk")
# 			# get record
# 			# convert to dictionary named x
# 			# x[typeTable] = data
# 			z = ["OK",data]
# 		except:
# 			z = ["NOK"]
# 		return HttpResponse(simplejson.dumps(z), content_type='application/json')
# 	return render(request,'Projects.html',{'category':int(str(request.session["category"]))})#int(str(request.session["category"]))
@login_required(login_url='/')
def student(request):
#	data = simplejson.loads(markList.objects.get(student = student.objects.get(userid=str(request.session["userid"]))).evalData)
#	context = {'userid':,'name':,'data':}
#	data = [[courseCode,title,asd]]
#	asd = {tabname:tabdata}
#	tabdata = {fieldname:value}	
	try:
		uid = str(request.session["userid"])
		usr  = userData.objects.get(userid = uid)
		dall = markList.objects.filter(student = studentData.objects.get(user = usr))
		dataLst = []
		for dd in dall:
			ed = dd.evalData
			ed = simplejson.loads(ed)
			for x in ed:
				if type(ed[x]) is unicode:
					ed[x] = simplejson.loads(ed[x])
			newed = {}
			for key in ed:
				x = ed[key]
				print x
				ined = {} 
				for key2 in x:
					print "@#@!#@$#@$@#",
					ined[nameDict[key2]] = x[key2]
				newed[key] = ined
			# print ed
			dataLst.append([dd.course.courseCode,dd.course.title,newed,dd.midSemGrade])
		context = {'data':dataLst,'bitsid':usr.bitsid,'name':usr.name,'category':int(request.session["category"])}
		return render(request,'student.html',context)	
	except Exception,e:
		print e
		return HttpResponse("ERROR!!!!! CONTACT DEVELOPER")

@login_required(login_url='/')
def reportDisp(request):
	if request.is_ajax():
		comment = request.GET.get("comment")
		idx = request.GET.get("id")
		data = ["OK",comment]
		return HttpResponse(simplejson.dumps(data),content_type='application/json')
	else:
		raise Http404
@login_required(login_url='/')
def reportGen(request):
	return render(request,'genReport.html',{'type':str(request.GET.get('type')),'category':int(str(request.session["category"]))})
@login_required(login_url='/')
def reminder(request):
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

def reportSubmit(request):
	if request.method =="POST":
		try:
			typ = str(request.GET.get("type"))
			pk = str(request.GET.get("id"))
			x = markList.objects.get(pk = pk)
			try:
				f1 = request.FILES["report"+pk]
			except:
				f1 = None
			try:
				f2 = request.FILES["antiPlag"+pk]
			except:
				f2  = None
			if typ == "1":
				x.midsemReport = f1
				x.midsemAntiPlag = f2
			elif typ =="2":
				x.endsemReport = f1
				x.endsemAntiPlag = f2
			x.save()
			return redirect('/grade/submitReport')
		except Exception,e:
			print e
			return HttpResponse("ERROR!!!!! contact Developers")
	else:
		try:
			uid  = str(request.session["userid"])
			x = userData.objects.get(userid=uid)
			ds = markList.objects.filter(faculty = facultyData.objects.get(user = x))
			lst = []
			for u in ds:
				lst1 = [u.pk,u.student.user.bitsid,u.student.user.name,u.course.courseCode,u.course.title]
				if u.midsemReport:
					lst1.append('/media/'+u.midsemReport.name)
				else:
					lst1.append('')
				if u.midsemAntiPlag:
					lst1.append('/media/'+u.midsemAntiPlag.name)
				else:
					lst1.append('')
				if u.endsemReport:
					lst1.append('/media/'+u.endsemReport.name)
				else:
					lst1.append('')
				if u.endsemAntiPlag:
					lst1.append('/media/'+u.endsemAntiPlag.name) 
				else:
					lst1.append('')
				lst.append(lst1)
			context = {'data':lst,'category':int(request.session["category"])}	
			return render(request,'SubmitReport.html',context)
		except Exception,e:
			print e
			return HttpResponse("Error!!!!! Contact Developers")
# def midSemReport(request):
# 	if not AccessPermission('key4',int(str(request.session["category"]))):
# 		raise Http404
# 	if request.method=='POST':
# 		token = False
# 		print request.GET.get('type')
# 		print request.GET.get('id')
# 		if request.FILES:
# 			return redirect('/grade/midSemReport?token=1')
# 		else:
# 			return redirect('/grade/midSemReport?token=0')
# 	else:
# 		token = request.GET.get('token',None)
# 		if token:
# 			return render(request,'midSemReport.html',{'token':token})
# 		else:	
# 			return render(request,'midSemReport.html',{'category':int(str(request.session["category"]))})
@login_required(login_url='/')
def courses(request):
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