from django.conf.urls import patterns, include, url
from apps.illuminaapi.views import analyzeView,illuminaView,runView

urlpatterns = [

	    url(r'^run/$',runView.RunList.as_view(),name='run-list'),
	    url(r'^run/(?P<pk>[0-9]+)/$', runView.RunDetail.as_view(),name='run-detail'),

	    url(r'^illumina/$', illuminaView.IlluminaList.as_view(),name='illumina-list'),
	    url(r'^illumina/(?P<pk>[0-9]+)/$', illuminaView.IlluminaDetail.as_view(),name='illumina-detail'),

	    url(r'^illumina/uploadcsv/$', illuminaView.upload,name='illumina-post-csv'),

	    url(r'^analyze/$', analyzeView.AnalyzeList.as_view(),name='analyze-list'),
	    url(r'^analyze/(?P<pk>[0-9]+)/$', analyzeView.AnalyzeDetail.as_view(),name='analyze-detail'),


]

