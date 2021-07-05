from os import truncate
from re import S, search
from flask import Flask, render_template, redirect, request, send_file,jsonify
from bs4 import BeautifulSoup
import csv
import requests
import string
import random
from collections import defaultdict


S = 6
ran = ''.join(random.choices(string.ascii_lowercase, k=S))
ran = str(ran)
ran = ran + ".csv"
print(ran)  # print the random data

app = Flask(__name__)


dict = defaultdict(list)
def completesearch(search_url):
    URL = search_url
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

    with open(ran, 'w') as f:
        write = csv.writer(f)
        count = 0
        for i in name:

            dict[count].append(i.text)
            count = count + 1
            #write.writerow(i)

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
            #write.writerow(w[0].split(","))
            dict[count].append(w[0].split(","))
            count = count + 1

        count = 0
        for i in rating:
            #write.writerow(i)
            dict[count].append(i.text)
            count = count + 1

        count = 0
        str = ""
        for i in num:
            if i.has_attr("class"):
                if(i['class'][1]) == 'resultimg':
                    q = str.split(",")
                    if q==[""]:
                        continue
                    dict[count].append(q)
                    count = count + 1
                    #write.writerow(q)
                    str = ""
                    continue
                if len(i['class']) != 0:
                    q = (di[i['class'][1]])
                    str = str+q

        count = 0
        for i in img:
            temp = i['data-src']
            temp1 = temp.split(",")
            dict[count].append(temp1)
            count = count + 1

            #write.writerow(temp1)
        for i in dict:
            write.writerow(dict[i])


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
    return jsonify(dict)


@app.route('/download')
def download_file():
    p = ran
    return send_file(p, as_attachment=True)


'''
@app.route('/search/')
def searchitem()
    return "task done"
'''
if __name__ == "__main__":
    app.run(debug=True)


'''
the csv file can be rendered at the next page and will give a download link
search item will do all the task and take url and make csv file
'''
