from rest_framework import generics
from rest_framework import mixins
from rest_framework import APIView
from apps.illuminaapi.models import Illumina
from apps.illuminaapi.serializers import IlluminaSerializer

class IlluminaList(generics.ListCreateAPIView):
	queryset = Illumina.objects.all()
	serializer_class = IlluminaSerializer

class IlluminaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Illumina.objects.all()
	serializer_class = IlluminaSerializer