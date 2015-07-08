from django.conf.urls import patterns, url
from selfie.views import IndexView, PhotoListView, GiftsView, RulesView, SelfieCreateView, ThanksView, HowStartView, \
    PartnersView, ContactsView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'photos/', PhotoListView.as_view(), name="photo_list"),
    url(r'gifts/', GiftsView.as_view(), name="gifts"),
    url(r'rules/', RulesView.as_view(), name="rules"),
    url(r'upload/', SelfieCreateView.as_view(), name="upload_pic"),
    url(r'thanks/', ThanksView.as_view(), name="thank_you"),
    url(r'how_start/', HowStartView.as_view(), name="how_start"),
    url(r'partners/', PartnersView.as_view(), name="partners"),
    url(r'contacts/', ContactsView.as_view(), name="contacts")
)