from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic
from selfie.forms import SelfieForm
from selfie.models import Selfie


class IndexView(generic.TemplateView):
    template_name = 'selfie/index.html'


class PhotoListView(generic.ListView):
    model = Selfie
    template_name = "selfie/photo_list.html"

    def get_queryset(self):
        return Selfie.objects.filter(is_rated=True)


class GiftsView(generic.TemplateView):
    template_name = "selfie/gifts.html"


class RulesView(generic.TemplateView):
    template_name = "selfie/rules.html"


class HowStartView(generic.TemplateView):
    template_name = "selfie/how_start.html"


class SelfieCreateView(generic.CreateView):
    template_name = 'selfie/selfie_add.html'
    form_class = SelfieForm
    success_url = '/thanks/'

    def get_initial(self):
        self.initial.update({'request': self.request})

        return self.initial

class ThanksView(generic.TemplateView):
    template_name = "selfie/thanks.html"