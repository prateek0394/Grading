from django.db import models
from datetime import datetime

# Create your models here.
class appName(models.Model):
	appID = models.CharField(max_length = 3)
	appName = models.CharField(max_length = 30)

class appOnOff(models.Model):
	app = models.ForeignKey(appName)
	startDate = models.CharField(max_length = 20)
	endDate = models.CharField(max_length = 20)
	timestamp = models.CharField(max_length = 20,default=str(datetime.now))