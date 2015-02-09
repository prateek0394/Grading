from django.db import models
from finalauth.models import *
from datetime import datetime
# Create your models here.
def namefile(instance,filename):
 	#ext = filename.split('.')[-1]
 	if not filename=="None":
	    return os.path.join('Grading/%s/' %(instance.student.userid),filename)
	else:
	    return None

class duration(models.Model):
	semester = models.IntegerField(max_length =1)
	year = models.IntegerField(max_length = 4)
	class Meta:
		unique_together =('semester','year')

class course(models.Model):
	courseCode = models.CharField(max_length=10)
	title = models.CharField(max_length = 30)

class markList(models.Model):
	student = models.ForeignKey(studentData)
	faculty = models.ForeignKey(facultyData)
	course = models.ForeignKey(course)
	dur = models.ForeignKey(duration)
	midSemGrade = models.CharField(max_length = 1)
	endSemGrade =  models.CharField(max_length = 1)
	evalData = models.TextField()
	midsemReport = models.FileField(upload_to=namefile)
	midsemAntiPlag = models.FileField(upload_to=namefile)
	endsemReport = models.FileField(upload_to=namefile)
	endsemAntiPlag = models.FileField(upload_to=namefile)

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
