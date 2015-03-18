from rest_framework import serializers
from apps.illuminaapi.models import Run,Illumina,Analyze


class RunSerializer(serializers.HyperlinkedModelSerializer):
	analyzes = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='analyze-detail')
	class Meta:
		model = Run
		fields = ('id','name','illumina','date','isFinished','analyzes')

class IlluminaSerializer(serializers.ModelSerializer):
	runs = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='run-detail')
	class Meta:
		model = Illumina
		fields = ('id','name','date','runs')

class AnalyzeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Analyze
		fields = ('id','name','run','csv','configuration','url','status')


