from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.illuminaapi.models import Analyze, Illumina, Job
from apps.illuminaapi.serializers import AnalyzeSerializer, JobSerializer
from apps.illuminaapi.scripts import createfastq
#from apps.illuminaapi.tasks import fastq_async
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import json
import sys
import magic

class AnalyzeViewSet(viewsets.ModelViewSet):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer
	parser_classes = (JSONParser,MultiPartParser, FormParser)
	def create(self,request):
		try:
			res=Response()
			data=request.DATA
			experiment_name = data['name']
			#If file is bein uploaded with form-data, the 'csv' field is not popluated with null!
			#We need to add the csv field to the data from the request and than add to the model the file.

			#Adding a csv field
			data['csv'] = None
			AnalyzeObject = AnalyzeSerializer(data=data,context={'request':request})
	 		if AnalyzeObject.is_valid():
	 			file_obj = request.FILES['csv']
	 			mime = magic.Magic(mime=True)
	 			if not (mime.from_buffer(file_obj.read()) in ['application/vnd.ms-excel','text/csv','text/plain']):
	 				raise Exception("Uploaded file should be a csv format")
	 			analyzeModel=AnalyzeObject.save(csv=file_obj)
	 			jobID = self.create_job_for_analyze(request, analyzeModel)
	 			res.data = "a job has been created"
	 			res.status_code=status.HTTP_202_ACCEPTED
	 			res['Location']="/illuminaapai/job/%s/" % jobID
	 			return res
	 		print "errors after not valid: %s" %(AnalyzeObject.errors)
	 		raise Exception(AnalyzeObject.errors)
		except Exception,e:
			#delete the model if created
			try:
				current_experiment = Analyze.objects.get(name=experiment_name)
				current_experiment.delete()
			except:
				pass
			finally:
				res.data="An error has been occured while creating new analyze: %s"%e.message
		 		res.status_code = status.HTTP_400_BAD_REQUEST
				return res

	def create_job_for_analyze(self,request, analyzeModel):
		jobObject = Job(analyze=analyzeModel,description="Start Running...")
		jobObject.save()
		# data = request.DATA
		# data['job_id'] = str(jobObject.id)
		# data['illumina_name'] = "data2"
		########task=fastq_async.delay(data) run with celery#######
		return jobObject.id


# class AnalyzeList(generics.ListCreateAPIView):
# 	queryset = Analyze.objects.all()
# 	serializer_class = AnalyzeSerializer

# 	def create(self,request,*args,**kwargs):
# 		data = request.DATA
# 		res = Response()
# 		AnalyzeObject = AnalyzeSerializer(data=data,context={'request':request})
# 		if AnalyzeObject.is_valid():
# 			analyzeModel=AnalyzeObject.save()
# 			jobID = self.create_job_for_analyze(request, analyzeModel)
# 			res.data = "a job has been created"
# 			res.status_code=status.HTTP_202_ACCEPTED
# 			res['Location']="/illuminaapai/job/%s/" % jobID
# 			return res
# 		res.data = AnalyzeObject.errors
# 		res.status_code = status.HTTP_400_BAD_REQUEST
# 		return res

# 	def create_job_for_analyze(self,request, analyzeModel):
# 		jobObject = Job(analyze=analyzeModel,description="Start Running...")
# 		jobObject.save()
# 		data = request.DATA
# 		data['job_id'] = str(jobObject.id)
# 	 	data['illumina_name'] = "data2"
# 	 	task=fastq_async.delay(data) #run with celery
# 	 	return jobObject.id

# class AnalyzeDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Analyze.objects.all()
# 	serializer_class = AnalyzeSerializer