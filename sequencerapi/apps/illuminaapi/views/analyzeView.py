from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
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

	def create(self,request,*args,**kwargs):
		data = request.DATA
		AnalyzeObject = AnalyzeSerializer(data=data,context={'request':request})
		if AnalyzeObject.is_valid():
			analyzeModel=AnalyzeObject.save()
	 		data['analyze_id'] = str(analyzeModel.id)
	 		data["illumina_name"] = "data2"
	 		createfastq.run(data)
	 		analyzeModel.status = "Finished"
	 		analyzeModel.save()
			return Response(AnalyzeObject.data,status=status.HTTP_201_CREATED)
		return Response(AnalyzeObject.errors,status=status.HTTP_400_BAD_REQUEST)


	def perform_create(self,serializer):
		"""
			This function is called by AnalyzeSerializer.create() method, just before
			saving the object.
			serializer parameter is the deserialized Analyze
			object based on the JSON self.request.data 
		"""
	 	data=self.request.data2
	 #	illuminaName = Illumina.objects.get(id=data['illumina_id']).name
	 	data["illumina_name"] = "data2"	 	
 		analyzeModel = serializer.save()
 		data['analyze_id'] = analyzeModel.id
 		createfastq.run(data)
 		analyzeModel.status = "Finished"
 		analyzeModel.save()

class AnalyzeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer


# class AnalyzeViewSet(viewsets.ModelViewSet):
# 	queryset = Analyze.objects.all()
# 	serializer_class = AnalyzeSerializer


