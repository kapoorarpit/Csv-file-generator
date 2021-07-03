from collections import namedtuple
from re import S, template
from bs4 import BeautifulSoup
import csv

import requests

URL = "https://www.justdial.com/Delhi/Restaurants-in-Indirapuram/nct-10408936"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
r = requests.get(URL,headers=header)
#print(r.content) 


soup = BeautifulSoup(r.text, features='html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib

vote = soup.select('span.rt_count',{'class':'cntanr'})
name = soup.select('span.lng_cont_name',{'class':'cntanr'})
rating = soup.select('span.green-box',{'class':'cntanr'})
num = soup.select('span.mobilesv,i.res_contactic.resultimg',{'class':'contact-info'})
img = soup.select('img.altImgcls', {'class':'cntanr'})

#rating = soup.select('span.green-box',{'class':'cntanr'})

#----------------------
di = {'icon-acb': '0', 'icon-yz': '1','icon-acb': '0', 'icon-wx': '2', 'icon-vu': '3', 'icon-ts': '4','icon-rq': '5', 'icon-po': '6','icon-nm': '7', 'icon-lk': '8','icon-ji': '9', 'icon-ba': '-','icon-hg': ')', 'icon-fe': '(','icon-dc': '+' }
#-----------------------------------------------

with open('data.csv', 'w') as f:
    write= csv.writer(f)
    for i in name:
        write.writerow(i)
        
    for i in vote:
        temp= i.get_text().strip()
        q = temp.split(",")
        w = q[0].split("\t")
        write.writerow(w[0].split(","))

    for i in rating:
        write.writerow(i)

    str= ""
    for i in num:
        if i.has_attr( "class" ):
            if(i['class'][1])=='resultimg':
                q = str.split(",")
                write.writerow(q)
                str=""
                continue
            if len( i['class'] ) != 0:
                q=(di[i['class'][1]])
                str = str+q

    for i in img:
        temp = i['data-src']
        temp1 = temp.split(",")
        write.writerow(temp1)

'''
data = response.text
    soup = BeautifulSoup(data, features='html.parser')

file = "data.csv"

with open(file, 'w') as csvfile:
    writer1 = csv.writer(csvfile)
    writer1.writerows(r)
    writer1.writerow(r)
'''
