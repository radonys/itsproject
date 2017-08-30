from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index,name="index"),
	url(r'^households/', views.funchid,name="households"),
	url(r'^farms/', views.farms,name="farms"),
	url(r'^photos/', views.photos,name="photos"),
	url(r'^members/', views.members,name="members"),
	url(r'^admin/', admin.site.urls),
]
