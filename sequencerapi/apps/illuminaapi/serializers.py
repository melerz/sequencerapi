from rest_framework import serializers
from apps.illuminaapi.models import Illumina,Analyze,Job


class IlluminaSerializer(serializers.ModelSerializer):
	analyzes = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='analyze-detail')
	class Meta:
		model = Illumina
		fields = ('name','date','analyzes')

class AnalyzeSerializer(serializers.HyperlinkedModelSerializer):
	created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
	job = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='job-detail')
	class Meta:
		model = Analyze
		fields = ('name','illumina','created','csv','url','status','job')


class JobSerializer(serializers.HyperlinkedModelSerializer):
	created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
	class Meta:
		model = Job
		fields = ('id','analyze','created','status','description')