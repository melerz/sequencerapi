from rest_framework import generics
from rest_framework import mixins
from rest_framework import APIView
from apps.illuminaapi.models import Analyze
from apps.illuminaapi.serializers import AnalyzeSerializer

class AnalyzeList(generics.ListCreateAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer

class AnalyzeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Analyze.objects.all()
	serializer_class = AnalyzeSerializer