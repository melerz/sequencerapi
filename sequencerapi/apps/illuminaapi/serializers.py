from rest_framework import serializers
from apps.illuminaapi.models import Run,Illumina,Analyze

class RunSerializer(serializers.ModelSerializer):
	class Meta:
		model = Run
		fields = ('id','name','illumina_id','date','isFinished')

class IlluminaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Illumina
		fields = ('id','name','date')

class AnalyzeSerializer(serializers.ModelSerializer):
	class Meta:
		moel = Analyze
		fields = ('id','name','run_id','csv','isFinished','url')


