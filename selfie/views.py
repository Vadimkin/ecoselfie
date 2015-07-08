from django.core.urlresolvers import reverse
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

class PartnersView(generic.TemplateView):
    template_name = "selfie/partners.html"

class ContactsView(generic.TemplateView):
    template_name = "selfie/contacts.html"

class SelfieCreateView(generic.CreateView):
    template_name = 'selfie/selfie_add.html'
    form_class = SelfieForm
    # success_url = reverse('thank_you')

    def get_initial(self):
        self.initial.update({'request': self.request})

        return self.initial

    def get_context_data(self, **kwargs):
        context = super(SelfieCreateView, self).get_context_data(**kwargs)

        user_selfies = Selfie.objects.filter(user__username=self.request.user)

        moderated_count = 0
        balls_count = 0
        all_count = len(user_selfies)

        for one_selfie in user_selfies:
            if one_selfie.is_rated:
                moderated_count += 1
                balls_count += one_selfie.balls

        context['moderated_count'] = moderated_count
        context['balls_count'] = balls_count
        context['all_count'] = all_count

        return context



class ThanksView(generic.TemplateView):
    template_name = "selfie/thanks.html"