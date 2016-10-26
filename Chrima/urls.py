from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<Cheque_id>[0-9]+)/$', views.Cheque, name='Cheque'),
    # ex: /polls/5/results/
    url(r'^(?P<Factura_id>[0-9]+)/Factura/$', views.Factura, name='Factura'),
    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]