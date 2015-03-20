from django.db import models
from jsonfield import JSONField
# Create your models here.

def get_status():
	return "running"

# class Run(models.Model):
# 	name = models.CharField(max_length=100)
# 	illumina = models.ForeignKey('Illumina',related_name='runs')
# 	date = models.DateTimeField(auto_now_add=True)
# 	isFinished = models.BooleanField(default=False)

# 	def __unicode__(self):
# 		return self.name

class Illumina(models.Model):
	name = models.CharField(primary_key=True,max_length=100)
	date = models.DateField()

	def __unicode__(self):
		return self.name

class Analyze(models.Model):
	name   = models.CharField(max_length=100)
	illumina = models.ForeignKey('Illumina',related_name='analyzes')
	created = models.DateTimeField(auto_now_add=True)
	csv = models.CharField(max_length=200)
	url = models.CharField(max_length=200,blank=True)
	status = models.CharField(max_length=200,default=get_status)
	#csv_file = models.FileField(upload_to='files/%Y/%m/%d') #someday
	configuration = JSONField(blank=True)

	def __unicode__(self):
		return self.name





