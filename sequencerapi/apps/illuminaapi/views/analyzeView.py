from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from apps.illuminaapi.models import Analyze, Illumina, Job
from apps.illuminaapi.serializers import AnalyzeSerializer, JobSerializer
from django.http import HttpResponse
from apps.illuminaapi.scripts import createfastq
from apps.illuminaapi.tasks import fastq_async
import json
import sys

class AnalyzeList(generics.ListCreateAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer

	def create(self,request,*args,**kwargs):
		data = request.DATA
		res = Response()
		AnalyzeObject = AnalyzeSerializer(data=data,context={'request':request})
		if AnalyzeObject.is_valid():
			analyzeModel=AnalyzeObject.save()
			jobID = self.create_job_for_analyze(request, analyzeModel)
			res.data = "a job has been created"
			res.status_code=status.HTTP_202_ACCEPTED
			res['Location']="/illuminaapai/job/%s/" % jobID
			return res
		res.data = AnalyzeObject.errors
		res.status_code = status.HTTP_400_BAD_REQUEST
		return res

	def create_job_for_analyze(self,request, analyzeModel):
		jobObject = Job(analyze=analyzeModel,description="Start Running...")
		jobObject.save()
		data = request.DATA
		data['job_id'] = str(jobObject.id)
	 	data['illumina_name'] = "data2"
	 	#task=fastq_async.delay(data) #run with celery
	 	createfastq.run(data)
	 	return jobObject.id

class AnalyzeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer


	# def perform_create(self,serializer):
	# 	"""
	# 		This function is called by AnalyzeSerializer.create() method, just before
	# 		saving the object.
	# 		serializer parameter is the deserialized Analyze
	# 		object based on the JSON self.request.data 
	# 	"""
	#  	data=self.request.data2
	#  #	illuminaName = Illumina.objects.get(id=data['illumina_id']).name
	#  	data["illumina_name"] = "data2"	 	
 # 		analyzeModel = serializer.save()
 # 		data['analyze_id'] = analyzeModel.id
 # 		createfastq.run(data)
 # 		analyzeModel.status = "Finished"
 # 		analyzeModel.save()



# class AnalyzeViewSet(viewsets.ModelViewSet):
# 	queryset = Analyze.objects.all()
# 	serializer_class = AnalyzeSerializer


