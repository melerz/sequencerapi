from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from apps.illuminaapi.models import Run
from apps.illuminaapi.serializers import RunSerializer

class RunList(generics.ListCreateAPIView):
	queryset = Run.objects.all()
	serializer_class = RunSerializer

class RunDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Run.objects.all()
	serializer_class = RunSerializer