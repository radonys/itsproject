from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
	return render(request,"restapi/index.html")
def funchid(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('http://10.0.3.23:8003/households/',data={"HID":h})
		r = True
		return render(request,'restapi/households.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/households.html',{ "r": r })
def members(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('http://10.0.3.23:8003/members/',data={"HID":h})
		r = True
		return render(request,'restapi/members.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/members.html',{ "r": r })
def farms(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('http://10.0.3.23:8003/farms/',data={"HID":h})
		r = True
		return render(request,'restapi/farms.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/farms.html',{ "r": r })
def photos(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('http://10.0.3.23:8003/photos/',data={"HID":h})
		r = True
		return render(request,'restapi/photos.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/photos.html',{ "r": r })
def crops(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('http://10.0.3.23:8003/crops/',data={"HID":h})
		r = True
		return render(request,'restapi/crops.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/crops.html',{ "r": r })

def area_data(request):
	r=False
	if request.POST:
		h=request.POST['ID'] #change to appropriate ID
		data = requests.post('http://10.0.3.23:8003/housedat/'+str(h)+'/')
		r = True
		return render(request,'restapi/maps.html',{"r": r, "data":data.text})
	else:
		return render(request,'restapi/maps.html',{ "r": r})
def area_all(request):
	data = requests.post('http://10.0.3.23:8003/houseall/')	#change housea accordingly
	r = True
	return render(request,'restapi/mapsall.html',{"r":r, "data":data.text})
def map_3d(request):
	# data = requests.post('http://10.0.3.23:8003/wells/')	#change housea accordingly
	r = True
	data1 = requests.post('http://10.0.3.23:8003/houseall/')
	return render(request,'restapi/3d.html',{"data1":data1.text,"r":r})
def map_3d2(request):
	# data = requests.post('http://10.0.3.23:8003/wells/')	#change housea accordingly
	# r = True
	return render(request,'restapi/3d2.html',{});
def charts(request):
	r=True
	return render(request,'restapi/charts.html',{"r":r})
def notpiechart(request):
	r=True
	return render(request,'restapi/notpiechart.html',{"r":r})
def circles(request):
	data = requests.post('http://10.0.3.23:8003/houseall/')	#change housea accordingly
	r = True
	return render(request,'restapi/housecircles.html',{"r":r, "data":data.text})
def cropsug(request):
	return render(request,'restapi/crop_suggest.html',{})
def polman(request):
	return render(request,'restapi/poultry_manage.html',{})
def properties_m(request):
	return render(request,'restapi/properties.html',{})
