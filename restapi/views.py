from django.shortcuts import render,HttpResponse
import requests
import html
import json
from xml.etree import ElementTree as et
from django.http import JsonResponse
import csv
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
'''
		Final views shown on website
1.Index
	Renders the request to the mainpage(index.html)
2.map3d
	Gets data from server and renders it on 3d map.
3.charts
	Displays bar graphs on index page
4.notpiechart
	Displays doughnut chart on poultry page
5.circles
	Gets the data of houses from server and renders it on 2d map
6.cropsug
	Displays crop suggestions on website
7.polman
	Renders poultry managemenet page
8.properties_m
	Renders the 3d map and the 2 2d maps.
'''
SERVER_URL = "https://farmereverywhere-server.herokuapp.com"
def index(request):
	return render(request,"restapi/index.html")
def funchid(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post(SERVER_URL+'/households/',data={"HID":h})
		r = True
		return render(request,'restapi/households.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/households.html',{ "r": r })
def members(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post(SERVER_URL+'/members/',data={"HID":h})
		r = True
		return render(request,'restapi/members.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/members.html',{ "r": r })
def farms(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post(SERVER_URL+'/farms/',data={"HID":h})
		r = True
		return render(request,'restapi/farms.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/farms.html',{ "r": r })
def photos(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post(SERVER_URL+'/photos/',data={"HID":h})
		r = True
		return render(request,'restapi/photos.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/photos.html',{ "r": r })
def crops(request):
	r=False
	if request.POST:
		h=request.POST['HID']
		data = requests.post(SERVER_URL+'/crops/',data={"HID":h})
		r = True
		return render(request,'restapi/crops.html',{ "r": r ,"data":data.text,"h":h })
	else:
		return render(request,'restapi/crops.html',{ "r": r })

def area_data(request):
	r=False
	if request.POST:
		h=request.POST['ID'] #change to appropriate ID
		data = requests.post(SERVER_URL+'/housedat/'+str(h)+'/')
		r = True
		return render(request,'restapi/maps.html',{"r": r, "data":data.text})
	else:
		return render(request,'restapi/maps.html',{ "r": r})
def area_all(request):
	data = requests.post(SERVER_URL+'/houseall/')	#change housea accordingly
	r = True
	return render(request,'restapi/mapsall.html',{"r":r, "data":data.text})
def map_3d(request):
	r = True
	data1 = requests.post(SERVER_URL+'/houseall/')
	return render(request,'restapi/3d.html',{"data1":data1.text,"r":r})
def map_3d2(request):
	# data = requests.post(SERVER_URL+'/wells/')	#change housea accordingly
	# r = True
	return render(request,'restapi/3d2.html',{})
def charts(request):
	r=True
	return render(request,'restapi/charts.html',{"r":r})
def notpiechart(request):
	r=True
	return render(request,'restapi/notpiechart.html',{"r":r})
def circles(request):
	data = requests.post(SERVER_URL+'/houseall/')	#change housea accordingly
	r = True
	return render(request,'restapi/housecircles.html',{"r":r, "data":data.text})
def cropsug(request):
	data = json.loads(requests.get("https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?format=json&api-key=579b464db66ec23bdd000001d85c100d2a4a49f760066d1e8bafe8dd&filters[state]=Andhra%20Pradesh&limit=10000").text)
	ref_data={}
	for i in data["records"]:
		if i["district"] not in ref_data:
			ref_data[i["district"]]={"date":i["arrival_date"]}
		else:
			ref_data[i["district"]][i["commodity"]]={"max_price":i["max_price"],"min_price":i["min_price"],"modal_price":i["modal_price"]}
	return render(request,'restapi/crop_suggest.html',{"data":json.dumps(ref_data)})
def polman(request):
	return render(request,'restapi/poultry_manage.html',{})
def properties_m(request):
	r = True
	data1 = requests.post(SERVER_URL+'/houseall/')
	return render(request,'restapi/properties.html',{"data1":data1.text})
def crop_details(request):
	links=["indiaagronet/crop info/wheat.htm", 'indiaagronet/crop info/bajra.htm', 'indiaagronet/crop info/maize.htm', 'indiaagronet/Crop_Husbandry/contents/soybean.htm', 'indiaagronet/crop info/green_gram.htm', 'indiaagronet/crop info/Ragi .htm', 'horticulture/CONTENTS/fenugreek.htm', 'horticulture/CONTENTS/black_pepper.htm', 'indiaagronet/crop info/Ocimum.htm', 'indiaagronet/horticulture/CONTENTS/Coriander.htm', 'indiaagronet/horticulture/CONTENTS/Curry Leaf.htm', 'horticulture/CONTENTS/cashew.htm', 'horticulture/CONTENTS/Garlic.htm', 'indiaagronet/crop info/ginger.htm', 'indiaagronet/crop info/bottlegourd.htm', 'indiaagronet/crop info/turmeric.htm', 'horticulture/CONTENTS/Beans.htm', 'indiaagronet/crop info/lemon grass.htm','indiaagronet/crop info/Cardamom.htm', 'horticulture/CONTENTS/Rubber.htm', 'indiaagronet/horticulture/CONTENTS/tea.htm']
	data=[]
	for x in links:
		data.append([x.split('/')[-1].split('.')[0].strip().title(),x.split('/')[-1],x.split('/')[-1].replace("htm","jpg")])
	print(data)
	json_list = json.dumps(data)
	return render(request,'restapi/crop_details.html',{"data":data})
def news(request):
	xmldata = requests.get("https://economictimes.indiatimes.com/news/economy/agriculture/rssfeeds/1202099874.cms").text
	print(xmldata)
	tree = et.fromstring(xmldata).find("channel").findall("item")
	newsarts = []
	for i in tree:
		temp_data = {}
		temp_data["title"] = i.find("title").text
		temp_data["link"] = i.find("link").text
		temp_data["description"] = i.find("description").text
		temp_data["date"] = i.find("pubDate").text
		temp_data["img"] = i.find("image").text
		newsarts.append(temp_data)
	return JsonResponse(newsarts,status=200,safe=False)
def crop_graphs(request):
	reader = csv.reader(open('apy.csv'))
	data=[]
	k_crops=[]
	b_crops=[]
	a_crops=[]
	for line in reader:
		data.append([x.strip() for x in line])
		s=line[3].strip()
		if(s=='Kharif'):
			k_crops.append(line[4])
		elif(s=="Rabi"):
			b_crops.append(line[4])
		else:
			a_crops.append(line[4])
	a_crops=list(set(a_crops))
	b_crops=list(set(b_crops))
	k_crops=list(set(k_crops))
	print(k_crops)

	print(b_crops)
	print(a_crops)
	print(set(b_crops)-set(k_crops))
	return render(request,'restapi/crop_graph.html',{"data":data,"a_crops":a_crops,"b_crops":b_crops,"k_crops":k_crops})
@csrf_exempt
def searchnews(request):
	if request.method=="POST":
		query = json.loads(request.body.decode('utf-8'))['query']
		print(query)
		xmldata = requests.get( "https://news.google.com/rss/search/section/q/"+query+"/"+query+"?hl=en-IN&gl=IN&ned=in").text
		newsarts = []
		tree = et.fromstring(xmldata).find("channel").findall("item")
		for i in tree:
			temp_data = {}
			if len(i.find("title"))>1:
				temp_data["title"] = i.find("title")[0].text
			else:
				temp_data["title"] = i.find("title").text
			if len(i.find("link"))>1:
				temp_data["link"] = i.find("link")[0].text
			else:
				temp_data["link"] = i.find("link").text
			if len(i.find("description"))>1:
				temp_data["description"] = i.find("description")[0].text
			else:
				temp_data["description"] = i.find("description").text
			if len(i.find("pubDate"))>1:
				temp_data["date"] = i.find("pubDate")[0].text
			else:
				temp_data["date"] = i.find("pubDate").text
			if i.find("image"):
				if len(i.find("image"))>1:
					temp_data["img"] = i.find("image")[0].text
				else:
					temp_data["img"] = i.find("image").text
			else:
				temp_data["img"]=newsarts.append(temp_data)
		return JsonResponse(newsarts,status=200,safe=False)
	else:
		return HttpResponse("Not Allowed",status=400)
def poultry_news(request):
	xmldata = requests.get("https://news.google.com/news/rss/search/section/q/Poultry%20India/Poultry%20India?hl=en-IN&gl=IN&ned=in").text#"https://economictimes.indiatimes.com/news/economy/agriculture/rssfeeds/1202099874.cms").text
	#print(xmldata)
	tree = et.fromstring(xmldata).find("channel").findall("item")
	newsarts = []
	for i in tree:
		temp_data = {}
		if len(i.find("title"))>1:
			temp_data["title"] = i.find("title")[0].text
		else:
			temp_data["title"] = i.find("title").text
		if len(i.find("link"))>1:
			temp_data["link"] = i.find("link")[0].text
		else:
			temp_data["link"] = i.find("link").text
		if len(i.find("description"))>1:
			temp_data["description"] = i.find("description")[0].text
		else:
			temp_data["description"] = i.find("description").text
		if len(i.find("pubDate"))>1:
			temp_data["date"] = i.find("pubDate")[0].text
		else:
			temp_data["date"] = i.find("pubDate").text
		if i.find("image"):
			if len(i.find("image"))>1:
				temp_data["img"] = i.find("image")[0].text
			else:
				temp_data["img"] = i.find("image").text
		newsarts.append(temp_data)
	return JsonResponse(newsarts,status=200,safe=False)
