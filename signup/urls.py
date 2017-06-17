from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^base/$', views.base),
    url(r'^$', views.sign),
    url(r'^base/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^one_time_password/$', views.one_time_password),
    url(r'^login/$', views.login),
    url(r'^ajax/email_validate/$', views.validate),
    url(r'^logout/$', views.logout),

]
