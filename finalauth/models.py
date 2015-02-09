from django.db import models
from datetime import datetime
import os
# Create your models here.
def namefile(instance,filename):
 	#ext = filename.split('.')[-1]
 	if not filename=="None":
	    return os.path.join('Userdata/%s' %(instance.operation),filename)
	else:
	    return None

class userData(models.Model):
	userid = models.CharField(max_length=10)
	bitsid = models.CharField(max_length = 14)
	name = models.CharField(max_length = 50)
	userType = models.IntegerField(max_length=1)

class studentData(models.Model):
	user = models.ForeignKey(userData)

class facultyData(models.Model):
	user = models.ForeignKey(userData)

class logForUsers(models.Model):
	user = models.ForeignKey(userData)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))

class uploadDelete(models.Model):
	operation = models.CharField(max_length = 30)
	uploadFile = models.FileField(upload_to=namefile)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))	