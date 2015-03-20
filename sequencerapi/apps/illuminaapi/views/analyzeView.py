from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from apps.illuminaapi.models import Analyze, Illumina
from apps.illuminaapi.serializers import AnalyzeSerializer
from django.http import HttpResponse
from apps.illuminaapi.scripts import createfastq
import json
import sys
class AnalyzeList(generics.ListCreateAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer

	# def create(self,request,*args,*kwargs):
	# 	data=request.DATA


	def perform_create(self,serializer):
		"""
			This function is called by AnalyzeSerializer.create() method, just before
			saving the object.
			serializer parameter is the deserialized Analyze
			object based on the JSON self.request.data 
		"""
	 	data=self.request.data
	 #	illuminaName = Illumina.objects.get(id=data['illumina_id']).name
	 	data["illumina_name"] = "data2"	 	
 		analyzeModel = serializer.save()
 		data['analyze-id'] = analyzeModel.id
 		createfastq.run(data)
 		analyzeModel.status = "Finished"
 		analyzeModel.save()

class AnalyzeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer


# class AnalyzeViewSet(viewsets.ModelViewSet):
# 	queryset = Analyze.objects.all()
# 	serializer_class = AnalyzeSerializer


