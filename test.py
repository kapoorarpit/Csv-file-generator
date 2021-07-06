import csv
from bs4 import BeautifulSoup
import requests


class list_item:
  def __init__(self):
    self.name = ""
    self.vote = ""  
    self.rating = ""
    self.num = ""
    self.img = ""

li = []

URL = "https://www.justdial.com/Delhi/Restaurants-in-Indirapuram/nct-10408936"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
r = requests.get(URL, headers=header)
# print(r.content)

# If this line causes an error, run 'pip install html5lib' or install html5lib
soup = BeautifulSoup(r.text, features='html.parser')

# --------------------------------------------

vote = soup.select('span.rt_count', {'class': 'cntanr'})
name = soup.select('span.lng_cont_name', {'class': 'cntanr'})
rating = soup.select('span.green-box', {'class': 'cntanr'})
num = soup.select('span.mobilesv,i.res_contactic.resultimg', {
                    'class': 'contact-info'})
img = soup.select('img.altImgcls', {'class': 'cntanr'})

# --------------------------------------------------
di = {'icon-acb': '0', 'icon-yz': '1', 'icon-acb': '0', 'icon-wx': '2', 'icon-vu': '3', 'icon-ts': '4', 'icon-rq': '5',
        'icon-po': '6', 'icon-nm': '7', 'icon-lk': '8', 'icon-ji': '9', 'icon-ba': '-', 'icon-hg': ')', 'icon-fe': '(', 'icon-dc': '+'}
# -----------------------------------------------

with open("data.csv", 'w') as f:
    write = csv.writer(f)
    for i in name:
        temp = list_item()
        setattr(temp, 'name', i.text)
        li.append(temp)

    count = 0
    even = 0
    for i in vote:
        if even == 1:
            even = 0
            continue
        else:
            even = 1
        temp = i.get_text().strip()
        q = temp.split(",")
        w = q[0].split("\t")
        setattr(li[count],'vote', w[0].split(","))
        count = count + 1

    count = 0
    for i in rating:
        setattr(li[count], 'rating', i.text)
        count = count + 1

    count = 0
    str = ""
    for i in num:
        if i.has_attr("class"):
            if(i['class'][1]) == 'resultimg':
                q = str.split(",")
                if q==[""]:
                    continue
                #dict[count].append(q)
                setattr(li[count], 'num', q)
                count = count + 1
                #write.writerow(q)
                str = ""
                continue
            if len(i['class']) != 0:
                q = (di[i['class'][1]])
                str = str+q
    q = str.split(",")
    setattr(li[count], 'num', q)

    count = 0
    for i in img:
        temp = i['data-src']
        temp1 = temp.split(",")
        #dict[count].append(temp1)
        setattr(li[count], 'img', temp1)
        count = count + 1

        #write.writerow(temp1)
    for i in li:
        print(i.name, i.vote, i.rating, i.num, i.img)
        
