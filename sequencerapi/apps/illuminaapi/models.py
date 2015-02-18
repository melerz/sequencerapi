from django.db import models

# Create your models here.


class Run(models.Model):
	name = models.CharField(max_length=100)
	illumina_id = models.ForeignKey('Illumina')
	date = models.DateTimeField(auto_now_add=True)
	isFinished = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

class Illumina(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField()

	def __unicode__(self):
		return self.name

class Analyze(models.Model):
	name   = models.CharField(max_length=100)
	run_id = models.ForeignKey('Run')
	isFinished = models.BooleanField(default=False)
	csv = models.CharField(max_length=200,default='')
	url = models.CharField(max_length=200,default='')

	def __unicode__(self):
		return self.name
