from django.conf.urls import patterns, url
from selfie.views import IndexView, PhotoListView, GiftsView, RulesView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'photos/', PhotoListView.as_view(), name="photo_list"),
    url(r'gifts/', GiftsView.as_view(), name="gifts"),
    url(r'rules/', RulesView.as_view(), name="rules")
)