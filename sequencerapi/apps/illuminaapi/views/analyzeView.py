from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from apps.illuminaapi.models import Analyze, Illumina
from apps.illuminaapi.serializers import AnalyzeSerializer
from django.http import HttpResponse
from apps.illuminaapi.scripts import createfastq
import json
class AnalyzeList(generics.ListCreateAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer

	def perform_create(self,serializer):
	 	data=json.loads(self.request.body)
	 	f=open("/tmp/tahat","r+w")
	 	f.write(str(data))
	 	illuminaName = Illumina.objects.get(id=data['illumina_id'])
	 	data["illumina_name"] = illuminaName
	 	createfastq.run(data)

class AnalyzeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer


# class AnalyzeViewSet(viewsets.ModelViewSet):
# 	queryset = Analyze.objects.all()
# 	serializer_class = AnalyzeSerializer


