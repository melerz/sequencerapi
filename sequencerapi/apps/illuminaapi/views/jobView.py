from rest_framework import viewsets
from rest_framework.response import Response
from apps.illuminaapi.models import Job
from apps.illuminaapi.serializers import JobSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class JobViewSet(viewsets.ModelViewSet):
	queryset = Job.objects.all()
	serializer_class = JobSerializer 