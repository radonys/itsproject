from django.conf.urls import url
from django.contrib import admin
from . import views
'''
	URL links to the respective views and HTML pages
'''
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^index/', views.index,name="index"),
	url(r'^$', views.index,name="index"),
	url(r'^crops/', views.crops,name="crops"),
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
    url(r'^3d2/', views.map_3d2,name="3d2"),
    url(r'^circles/', views.circles,name="circles"),
    url(r'^poultry/', views.notpiechart,name="notpiechart"),
  url(r'^properties/', views.properties_m,name="property"),
  url(r'^poultry_manage/', views.polman,name="poultry"),
  url(r'^cropsuggest/', views.cropsug,name="cropsug"),
  url(r'^cropdet/', views.crop_details,name="cropdet"),
]
