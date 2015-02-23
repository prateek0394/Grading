from django.db import models
from finalauth.models import *
from datetime import datetime
# Create your models here.
def namefile(instance,filename):
 	if not filename=="None":
	    return os.path.join('Grading/%s/' %(instance.student.user.userid),filename)
	else:
	    return None

class duration(models.Model):
	semester = models.IntegerField(max_length =1)
	year = models.IntegerField(max_length = 4)
	class Meta:
		unique_together =('semester','year')

class course(models.Model):
	courseCode = models.CharField(max_length=10,unique=True)
	title = models.CharField(max_length = 30)

class courseTemplates(models.Model):
	courseN = models.ForeignKey(course)
	keyDev = models.IntegerField(max_length=2)

class SFCD(models.Model):
	student = models.ForeignKey(studentData)
	faculty = models.ForeignKey(facultyData)
	course = models.ForeignKey(course)
	dur = models.ForeignKey(duration)

class markListData(models.Model):
	user = models.ForeignKey(userData)
	handle = models.ForeignKey(SFCD)
	evalData = models.TextField()
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class HODoverLoad(models.Model):
	user = models.ForeignKey(userData)
	reason = models.CharField(max_length=100)
	comment = models.TextField()
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class markListMidGrade(models.Model):
	user = models.ForeignKey(userData)
	handle = models.ForeignKey(SFCD)
	midSemGrade = models.CharField(max_length = 5)
	reason = models.TextField(default=None)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class markListEndGrade(models.Model):
	user = models.ForeignKey(userData)
	handle = models.ForeignKey(SFCD)
	endSemGrade = models.CharField(max_length = 5)
	reason = models.TextField(default=None)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class markListSeminarGrade(models.Model):
	user = models.ForeignKey(userData)
	handle = models.ForeignKey(SFCD)
	seminarGrade = models.CharField(max_length = 5)
	reason = models.TextField(default=None)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class studentMidReports(models.Model):
	user = models.ForeignKey(userData)
	handle = models.ForeignKey(SFCD)
	midsemReport = models.FileField(upload_to=namefile)
	midsemAntiPlag = models.FileField(upload_to=namefile)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class studentEndReports(models.Model):
	user = models.ForeignKey(userData)
	handle = models.ForeignKey(SFCD)
	endsemReport = models.FileField(upload_to=namefile)
	endsemAntiPlag = models.FileField(upload_to=namefile)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class reminder_details(models.Model):
	userid = models.ForeignKey(userData)
	reciever = models.CharField(max_length = 30)
	subject = models.CharField(max_length = 100)
	message = models.TextField()
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class reportGeneration(models.Model):
	userid = models.ForeignKey(userData)
	reportDesc = models.TextField()
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))