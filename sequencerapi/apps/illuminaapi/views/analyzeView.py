from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.illuminaapi.models import Analyze, Illumina, Job
from apps.illuminaapi.serializers import AnalyzeSerializer, JobSerializer
from apps.illuminaapi.scripts import createfastq
from apps.illuminaapi.tasks import fastq_async
import json
import sys

class AnalyzeViewSet(viewsets.ModelViewSet):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer

	def create(self,request):
		try:
			res=Response()
			data=request.DATA
			experiment_name = data['name']
			#/uploads(MEDIA_ROOT)/experiment_name/filename.csv / SampleSheet.csv
			experiment_dir_path = settings.MEDIA_ROOT+experiment_name
			if not os.path.isdir(experiment_dir_path):
				os.mkdir(experiment_dir_path)

			AnalyzeObject = AnalyzeSerializer(data=data,context={'request':request})
	 		if AnalyzeObject.is_valid():
	 			analyzeModel=AnalyzeObject.save()
	 			jobID = self.create_job_for_analyze(request, analyzeModel)
	 			res.data = "a job has been created"
	 			res.status_code=status.HTTP_202_ACCEPTED
	 			res['Location']="/illuminaapai/job/%s/" % jobID
	 			return res
	 		raise Exception(AnalyzeObject.errors)
		except Exception,e:
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