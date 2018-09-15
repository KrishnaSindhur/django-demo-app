from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView

urlpatterns = {
    url(r'^(?P<key>.*)$', DetailView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
