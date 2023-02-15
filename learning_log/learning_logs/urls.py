from django.urls import include, re_path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #主页
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$', views.topics, name="topics"),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name="topic")
]