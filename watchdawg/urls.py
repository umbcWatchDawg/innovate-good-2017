from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as djlogout
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', djlogout, name='logout'),
    url(r'^report$', login_required(views.report)),
]
