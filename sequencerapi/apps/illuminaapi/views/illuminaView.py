from rest_framework import viewsets
from apps.illuminaapi.models import Illumina
from apps.illuminaapi.serializers import IlluminaSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from apps.illuminaapi import upload_file
import json

class IlluminaViewSet(viewsets.ModelViewSet):
	queryset = Illumina.objects.all()
	serializer_class = IlluminaSerializer


# @csrf_exempt
# def upload(request):
# 	if request.method =='POST':
# 		return upload_post(request)

# def upload_post(request):
# 	response= HttpResponse()

# 	response['Content-Type'] = 'application/json'

# 	response['Access-Control-Allow-Origin'] = '*'

# 	response['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, PUT, DELETE'

# 	response['Access-Control-Allow-Headers'] = 'Content-Type, Content-Range, Content-Disposition'
	
# 	experiment_name = (request.DATA)['name']
# 	result=upload_file.handle_upload_file(experiment_name,request.FILES['files[]'])
# 	try:
# 		result.has_key('error')
# 		response.status_code = 403
# 		response.write(json.dumps(result))
# 		return response
# 	except:
# 		output = {'files':result}
# 		res_json = json.dumps(output)
# 		response.write(res_json)
# 		return response

# def options(self):
# 	pass