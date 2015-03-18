from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from apps.illuminaapi.models import Run
from apps.illuminaapi.serializers import RunSerializer
from django.db.models.signals import post_save
from django.http import HttpResponse
class RunList(generics.ListCreateAPIView):
	queryset = Run.objects.all()
	serializer_class = RunSerializer

	def post_save(sender,instance,created):
		if(created):
			return HttpResponse({"id":instance.id})
class RunDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Run.objects.all()
	serializer_class = RunSerializer