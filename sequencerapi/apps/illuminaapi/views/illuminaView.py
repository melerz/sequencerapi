from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from apps.illuminaapi.models import Illumina
from apps.illuminaapi.serializers import IlluminaSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
#from apps.illuminaapi.uploadHandler import UploadHandler

class IlluminaList(generics.ListCreateAPIView):
	queryset = Illumina.objects.all()
	serializer_class = IlluminaSerializer

class IlluminaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Illumina.objects.all()
	serializer_class = IlluminaSerializer



@csrf_exempt
def upload(request):
	if request.method =='POST':
		return upload_post(request)

def upload_post(request):
	response= HttpResponse()
	
	response['Access-Control-Allow-Origin'] = '*'

	response['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, PUT, DELETE'

	response['Access-Control-Allow-Headers'] = 'Content-Type, Content-Range, Content-Disposition'

	for name in request.POST.items():
		response+="%s:%s" %(name)
	return HttpResponse(response)

class IlluminaSampleSheetUpload(View):
	def get(self,request):
		self.redirect(WEBSITE)
	

	@method_decorator(csrf_exempt)
	def post(self,request,*args,**kwargs):
	    # if (self.request.get('_method') == 'DELETE'):
	    #     return self.delete()
	    # result = {'files': ''}
	    # s = json.dumps(result, separators=(',', ':'))
	    # redirect = self.request.get('redirect')
	    # if redirect:
	    #     return self.redirect(str(
	    #         redirect.replace('%s', urllib.quote(s, ''), 1)
	    #     ))
	    # if 'application/json' in self.request.headers.get('Accept'):
	    #     self.response.headers['Content-Type'] = 'application/json'
     	# self.response.write(s)
     	 super(IlluminaSampleSheetUpload,self).post(request,*args,**kwargs)
     	 return HttpResponse('result')
     	 
	     