from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^raiseQuestion/$', views.questionRaise, name='raiseQuestion'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/appreciate/$', views.appreciate, name='appreciate'),
    url(r'^rankByUpTime/$', views.rankByUpTime, name='rankByUpTime'),
    url(r'^rankByDownTime/$', views.rankByDownTime, name='rankByDownTime'),
    url(r'^rankByAppreciation/$', views.rankByAppreciation, name='rankByAppreciation'),
    url(r'^search/$', views.search, name='search'),
]
