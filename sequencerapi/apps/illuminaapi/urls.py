from django.conf.urls import patterns, include, url
from apps.illuminaapi.views import analyzeView,illuminaView,jobView

urlpatterns = [

	    url(r'^illumina/$', illuminaView.IlluminaList.as_view(),name='illumina-list'),

	    url(r'^illumina/uploadcsv/$', illuminaView.upload,name='illumina-post-csv'),

	    url(r'^illumina/(?P<pk>\w+)/$', illuminaView.IlluminaDetail.as_view(),name='illumina-detail'),


	    url(r'^analyze/$', analyzeView.AnalyzeList.as_view(),name='analyze-list'),

	    url(r'^analyze/(?P<pk>[0-9]+)/$', analyzeView.AnalyzeDetail.as_view(),name='analyze-detail'),

	    url(r'^job/$', jobView.JobList.as_view(),name='job-list'),
	    url(r'^job/(?P<pk>[0-9]+)/$', jobView.JobDetail.as_view(),name='job-detail'),


]

