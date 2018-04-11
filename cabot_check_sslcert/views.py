from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from cabot.cabotapp.models import StatusCheck
from cabot.cabotapp.views import (CheckCreateView, CheckUpdateView,
                                  StatusCheckForm, base_widgets)

from .models import SslcertStatusCheck


class SslcertStatusCheckForm(StatusCheckForm):
    symmetrical_fields = ('service_set', 'instance_set')

    class Meta:
        model = SslcertStatusCheck
        fields = (
            'name',
            'host',
            'common_name',
            'port',
            'days',
            'timeout',
            'frequency',
            'active',
            'importance',
            'debounce',
        )

        widgets = dict(**base_widgets)
        widgets.update({
            'host': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'service.arachnys.com',
            }),
            'common_name': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'service.arachnys.com',
            })
        })


class SslcertCheckCreateView(CheckCreateView):
    model = SslcertStatusCheck
    form_class = SslcertStatusCheckForm


class SslcertCheckUpdateView(CheckUpdateView):
    model = SslcertStatusCheck
    form_class = SslcertStatusCheckForm


def duplicate_check(request, pk):
    pc = StatusCheck.objects.get(pk=pk)
    npk = pc.duplicate()
    return HttpResponseRedirect(reverse('update-sslcert-check', kwargs={'pk': npk}))
