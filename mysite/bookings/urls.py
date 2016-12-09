from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.flight_list, name='list'),
	url(r'(?P<booking_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step'),
	url(r'(?P<pk>\d+)/$', views.booking_detail, name='detail'),
]