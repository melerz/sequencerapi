from django.db import models
from django.conf import settings
# Create your models here.

def get_status():
	return "running"


def get_upload_path(instance,filename):
	#neeed to remove SampleSheet.csv if it's already exist
	return "%s/%s"%(instance.name,"SampleSheet.csv")
		
class Illumina(models.Model):
	name = models.CharField(primary_key=True,max_length=100)
	date = models.DateField()

	def __unicode__(self):
		return self.name

class Analyze(models.Model):
	name   = models.CharField(primary_key=True,max_length=100)
	illumina = models.ForeignKey('Illumina',related_name='analyzes')
	created = models.DateTimeField(auto_now_add=True)
	url = models.CharField(max_length=200,blank=True)
	status = models.CharField(max_length=200,default=get_status)
	csv = models.FileField(upload_to=get_upload_path) #someday
	workflow   = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name



# class Workflow(models.Model):
# 	name   = models.CharField(primary_key=True,max_length=100)

# class Method(models.Model):
# 	name = models.CharField(primary_key=True,max_length=100)
# 	workflow = models.ForeignKey('Workflow',related_names='methods')

class Job(models.Model):
	analyze = models.ForeignKey('analyze',unique=True,related_name='job')
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=200,default=get_status) #Runnig,#Finished,#Failed
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s"%self.analyze.name





