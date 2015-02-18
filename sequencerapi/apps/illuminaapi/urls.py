from django.conf.urls import patterns, include, url
from apps.illuminaapi.views import analyzeView,illuminaView,runView

urlpatterns = patterns('',

    url(r'^run/$', include(runView.RunList.as_view())),
    url(r'^run/(?P<pk>[0-9]+)/$', include(runView.RunDetail.as_view())),

    url(r'^illumina/$', include(illuminaView.IlluminaList.as_view())),
    url(r'^illumina/(?P<pk>[0-9]+)/$', include(illuminaView.IlluminaDetail;.as_view())),

    url(r'^analyze/$', include(analyzeView.AnalyzeList.as_view())),
    url(r'^analyze/(?P<pk>[0-9]+)/$', include(analyzeView.AnalyzeDetail.as_view())),
)