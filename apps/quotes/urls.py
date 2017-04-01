from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^contribute$', views.contribute, name = "contribute"),
    url(r'^add_fav/(?P<id>\d+)$', views.add_fav, name = "add_fav"),
    url(r'^user/(?P<id>\d+)$', views.user, name = "user"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = "remove"),
    url(r'^logout', views.logout, name = "logout")
    ]
