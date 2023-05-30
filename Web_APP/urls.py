from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'Web_APP'

urlpatterns = [
    path('', views.home, name="home"),
    path('crops', views.crops, name="crops"),
    path('disease', views.disease, name="disease"),
    path('crop_result', views.crop_result, name="crop_result"),

    url(r'^wheat_disease/$', views.WheatDView.as_view(), name='wheat'),
    url(r'^wheat_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.WheatView.as_view(), name='wheat_disease'),

    url(r'^rice_disease/$', views.RiceDView.as_view(), name='rice'),
    url(r'^rice_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.RiceView.as_view(), name='rice_disease'),

    url(r'^potato_disease/$', views.PotatoDView.as_view(), name='potato'),
    url(r'^potato_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.PotatoView.as_view(), name='potato_disease'),


    url(r'^groundnut_disease/$', views.GroundnutDView.as_view(), name='groundnut'),
    url(r'^groundnut_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.GroundnutView.as_view(), name='groundnut_disease'),


    url(r'^pulses_disease/$', views.PulsesDView.as_view(), name='pulses'),
    url(r'^pulses_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.PulsesView.as_view(), name='pulses_disease'),


    url(r'^tomato_disease/$', views.TomatoDView.as_view(), name='tomato'),
    url(r'^tomato_disease/(?P<slug>[A-Za-z0-9_-]+)/$', views.TomatoView.as_view(), name='tomato_disease'),



    
]
