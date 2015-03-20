from rest_framework import serializers
from apps.illuminaapi.models import Illumina,Analyze


# class RunSerializer(serializers.HyperlinkedModelSerializer):
# 	analyzes = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='analyze-detail')
# 	class Meta:
# 		model = Run
# 		fields = ('id','name','illumina','date','isFinished','analyzes')

class IlluminaSerializer(serializers.ModelSerializer):
	analyzes = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='analyze-detail')
	class Meta:
		model = Illumina
		fields = ('name','date','analyzes')

class AnalyzeSerializer(serializers.HyperlinkedModelSerializer):
	created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
	class Meta:
		model = Analyze
		fields = ('id','name','illumina','created','csv','configuration','url','status')


