from os import truncate
from re import S, search
from flask import Flask, render_template, redirect, request, send_file,jsonify
from bs4 import BeautifulSoup
import csv
import requests
import string
import random
from json import JSONEncoder
import json



S = 6
ran = ''.join(random.choices(string.ascii_lowercase, k=S))
ran = str(ran)
ran = ran + ".csv"
print(ran)  # print the random data

app = Flask(__name__)

class list_item:
  def __init__(self):
    self.name = ""
    self.vote = ""  
    self.rating = ""
    self.num = ""
    self.img = ""

def obj_dict(obj):
    return obj.__dict__

json_string = ""


li = []

def completesearch(search_url):
    URL = search_url
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    r = requests.get(URL, headers=header)

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

    '''with open("data.csv", 'w') as f:
        write = csv.writer(f)'''
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
        setattr(li[count],'vote', (w[0].split(","))[0])
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
                setattr(li[count], 'num', q[0])
                count = count + 1
                str = ""
                continue
            if len(i['class']) != 0:
                q = (di[i['class'][1]])
                str = str+q
    q = str.split(",")
    setattr(li[count], 'num', q[0])

    count = 0
    for i in img:
        temp = i['data-src']
        temp1 = temp.split(",")
        setattr(li[count], 'img', temp1[0])
        count = count + 1

    '''for i in li:
        print(i.name, i.vote, i.rating, i.num, i.img)'''

    global json_string 
    json_string = ""
    json_string = json.dumps(li, default=obj_dict)
    x = json.loads(json_string)

    f = csv.writer(open("data.csv", "w"))
    f.writerow(["name", "vote", "rating", "num", "img"])
    for x in x:
        f.writerow([x["name"],
                    x["vote"],
                    x["rating"],
                    x["num"],
                    x["img"]])
    print(json_string)
#print(json_string)


@app.route('/submit_url', methods=['POST'])
def submit_url():
    search_url= request.get_json()
    print(search_url['url'])
    completesearch(search_url['url'])
    return 'successful', 201


@app.route('/download')
def give_data():
    global json_string 
    return json_string


@app.route('/download1')
def give_data1():
    global json_string 
    n = json_string
    json_string=""
    return n


if __name__ == "__main__":
    app.run(debug=True)
'''
# home page---------------
@app.route('/', methods=['POST', 'GET'])
def inde():
    if request.method == 'POST':
        search_url = request.form['searchURL']
        completesearch(search_url)
        print(search_url)

        return redirect('/alt/')
    return render_template('home.html')



@app.route('/alt/')
def na():
    return json_string


@app.route('/download')
def download_file():
    p = ran
    return send_file(p, as_attachment=True)

'''
