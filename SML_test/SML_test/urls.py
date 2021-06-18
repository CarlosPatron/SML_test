from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^admin/", admin.site.urls),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r"^boards/(\d+)/$", views.board_topics, name='board_topics'),
]