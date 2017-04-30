from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as djlogout
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', djlogout, {'next_page': views.index}, name='logout'),
    url(r'^report/$', login_required(views.report)),
    url(r'^victim-witness/$', login_required(views.victim_witness), name='victim_witness'),
    url(r'^crime-type/$', login_required(views.crime_type), name='crime_type'),
    url(r'^elements/$', login_required(views.elements), name='elements'),
    url(r'^questions/$', login_required(views.questions), name='questions'),
]
