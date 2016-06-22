# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
#
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^signup/$',views.Signup.as_view()),
    url(r'^load/$',views.Load.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
