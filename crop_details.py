import urllib.request
from bs4 import BeautifulSoup
from lxml import html
url='https://www.indiaagronet.com/Crop-Cultivation/'
content=urllib.request.urlopen(url).read()
page = html.fromstring(content)
links=[]
for link in page.xpath("//a"):
    links.append(link.get("href"))
links=links[8:-19]
url1='https://www.indiaagronet.com/'
links=['indiaagronet/crop info/wheat.htm', 'indiaagronet/crop info/bajra.htm', 'indiaagronet/crop info/maize.htm', 'indiaagronet/Crop_Husbandry/contents/soybean.htm', 'indiaagronet/crop info/green_gram.htm', 'indiaagronet/crop info/Ragi .htm', 'horticulture/CONTENTS/fenugreek.htm', 'horticulture/CONTENTS/black_pepper.htm', 'indiaagronet/crop info/Ocimum.htm', 'indiaagronet/horticulture/CONTENTS/Coriander.htm', 'indiaagronet/horticulture/CONTENTS/Curry Leaf.htm', 'horticulture/CONTENTS/cashew.htm', 'horticulture/CONTENTS/Garlic.htm', 'indiaagronet/crop info/ginger.htm', 'indiaagronet/crop info/bottlegourd.htm', 'indiaagronet/crop info/turmeric.htm', 'horticulture/CONTENTS/Beans.htm', 'indiaagronet/crop info/lemon grass.htm', 'indiaagronet/crop info/Cardamom.htm', 'horticulture/CONTENTS/Rubber.htm', 'indiaagronet/horticulture/CONTENTS/tea.htm']

for link in links:
    f=open(link.split("/")[-1],'w')
    url=url1+link
    content=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content)
    z=soup.findAll("div", { "class" : "space-clear" })
    if not len(z):
        z=soup.findAll("div", { "class" : "row space-clear" })
    for x in z:
        for section in x.findAll('h2'):
            print(section)
            if(str(section)):
                f.write(str(section)+"\n")
        for section in x.findAll('p'):
            print(section)
            if(str(section)):
                f.write(str(section)+"\n")
        for section in x.findAll('ul'):
            print(section)
            if(str(section)):
                f.write(str(section)+"\n")
        for section in x.findAll('table'):
            print(section)
            if(str(section)):
                f.write(str(section)+"\n")
