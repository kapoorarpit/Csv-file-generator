from os import truncate
from re import S, search
from flask import Flask,render_template,redirect,request,send_file
from bs4 import BeautifulSoup
import csv
import requests
import string    
import random  


S = 6
ran = ''.join(random.choices(string.ascii_lowercase, k = S))    
ran = str(ran)
ran = ran +".csv"
print(ran) # print the random data  


app =  Flask(__name__)


def completesearch(search_url):
    URL = search_url
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    r = requests.get(URL,headers=header)
    #print(r.content) 


    soup = BeautifulSoup(r.text, features='html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib

    #--------------------------------------------

    vote = soup.select('span.rt_count',{'class':'cntanr'})
    name = soup.select('span.lng_cont_name',{'class':'cntanr'})
    rating = soup.select('span.green-box',{'class':'cntanr'})
    num = soup.select('span.mobilesv,i.res_contactic.resultimg',{'class':'contact-info'})
    img = soup.select('img.altImgcls', {'class':'cntanr'})

    #--------------------------------------------------
    di = {'icon-acb': '0', 'icon-yz': '1','icon-acb': '0', 'icon-wx': '2', 'icon-vu': '3', 'icon-ts': '4','icon-rq': '5', 'icon-po': '6','icon-nm': '7', 'icon-lk': '8','icon-ji': '9', 'icon-ba': '-','icon-hg': ')', 'icon-fe': '(','icon-dc': '+' }
    #-----------------------------------------------

    with open(ran, 'w') as f:
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


#home page---------------
@app.route('/',methods=['POST', 'GET'])
def inde():
    if request.method == 'POST':
        search_url= request.form['searchURL']
        completesearch(search_url)
        print(search_url)

        return redirect('/alt/')
    return render_template('home.html')


@app.route('/alt/')
def na():
    return render_template('download_csv.html', filename=ran)

@app.route('/download')
def download_file():
    p = ran
    return send_file(p, as_attachment=True)

'''
@app.route('/search/')
def searchitem()
    return "task done"
'''
if __name__== "__main__":
    app.run(debug=True)



'''
the csv file can be rendered at the next page and will give a download link
search item will do all the task and take url and make csv file
'''