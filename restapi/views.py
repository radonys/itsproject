from django.shortcuts import render
import requests
# Create your views here.
def index(request):
	return render(request,"restapi/index.html")
def funchid(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('https://farmereverywhere-server.herokuapp.com/households/',data={"HID":h})
		r = True
		return render(request,'restapi/households.html',{ "r": r ,"data":data,"h":h })
	else:
		return render(request,'restapi/households.html',{ "r": r })
def members(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('https://farmereverywhere-server.herokuapp.com/members/',data={"HID":h})
		r = True
		return render(request,'restapi/members.html',{ "r": r ,"data":data,"h":h })
	else:
		return render(request,'restapi/members.html',{ "r": r })
def farms(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('https://farmereverywhere-server.herokuapp.com/farms/',data={"HID":h})
		r = True
		return render(request,'restapi/farms.html',{ "r": r ,"data":data,"h":h })
	else:
		return render(request,'restapi/farms.html',{ "r": r })
def photos(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('https://farmereverywhere-server.herokuapp.com/photos/',data={"HID":h})
		r = True
		return render(request,'restapi/photos.html',{ "r": r ,"data":data,"h":h })
	else:
		return render(request,'restapi/photos.html',{ "r": r })
def crops(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post('https://farmereverywhere-server.herokuapp.com/crops/',data={"HID":h})
		r = True
		return render(request,'restapi/crops.html',{ "r": r ,"data":data,"h":h })
	else:
		return render(request,'restapi/crops.html',{ "r": r })
		
	
