from django.forms import ModelForm
from selfie.models import Selfie


class SelfieForm(ModelForm):
    class Meta:
        model = Selfie
        fields = ['selfie_before', 'selfie_after']

    def __init__(self, *args, **kwargs):
        self.request = kwargs['initial']['request']

        super(SelfieForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

    def save(self, *args, **kwargs):
        kwargs['commit']=False

        obj = super(SelfieForm, self).save(*args, **kwargs)

        if self.request:
            obj.user_id = self.request.user.id

        obj.save()

        return obj