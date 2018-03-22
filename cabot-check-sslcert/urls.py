from django.conf.urls import url

from .views import (SslcertCheckCreateView, SslcertCheckUpdateView,
                    duplicate_check)

urlpatterns = [

    url(r'^sslcertcheck/create/',
        view=SslcertCheckCreateView.as_view(),
        name='create-sslcert-check'),

    url(r'^sslcertcheck/update/(?P<pk>\d+)/',
        view=SslcertCheckUpdateView.as_view(),
        name='update-sslcert-check'),

    url(r'^sslcertcheck/duplicate/(?P<pk>\d+)/',
        view=duplicate_check,
        name='duplicate-sslcert-check')

]
