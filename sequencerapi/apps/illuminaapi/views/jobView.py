from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from apps.illuminaapi.models import Job
from apps.illuminaapi.serializers import JobSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from apps.illuminaapi import upload_file
import json


class JobList(generics.ListCreateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer