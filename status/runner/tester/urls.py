# BuiltIn django and rest_framework packages
from django.conf.urls import url,patterns,include
from rest_framework.urlpatterns import format_suffix_patterns
# Custom defined packages
from tester import views

urlpatterns = [
    url(r'^user/$', views.Userss.as_view()),
    url(r'^userlog/$', views.UserLog.as_view()),
]
