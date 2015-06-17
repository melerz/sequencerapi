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
	status = serializers.CharField(read_only=True)
	csv = serializers.FileField(allow_empty_file=True,allow_null=True)
	class Meta:
		model = Analyze
		fields = ('name','illumina','created','csv','url','status','job')


class JobSerializer(serializers.HyperlinkedModelSerializer):
	created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
	class Meta:
		model = Job
		fields = ('id','analyze','created','status','description')