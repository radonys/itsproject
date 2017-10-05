from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index,name="index"),
	url(r'^households/', views.funchid,name="households"),
	url(r'^farms/', views.farms,name="farms"),
	url(r'^photos/', views.photos,name="photos"),
	url(r'^members/', views.members,name="members"),
	url(r'^crops/', views.crops,name="members"),
	url(r'^houses/', views.area_data,name="maps"),
	url(r'^housesall/', views.area_all,name="mapsall"),
    url(r'^3d/', views.map_3d,name="3d"),
	url(r'^housesall/', views.area_all,name="mapsall"),
	url(r'^charts/', views.charts,name="charts"),
    url(r'^poultry/', views.notpiechart,name="notpiechart")
]
