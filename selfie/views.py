from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'selfie/index.html'


class PhotoListView(generic.TemplateView):
    template_name = "selfie/photo_list.html"


class GiftsView(generic.TemplateView):
    template_name = "selfie/gifts.html"


class RulesView(generic.TemplateView):
    template_name = "selfie/rules.html"
