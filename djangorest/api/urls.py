from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^friends/$', views.CreateView.as_view(), name="create"),
    url(r'^all/$', views.listAll, name="listAll")
}

urlpatterns = format_suffix_patterns(urlpatterns)