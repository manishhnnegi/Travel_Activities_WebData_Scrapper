from flask import Flask,render_template, request, jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from modularproject.creatFilPath import *
from modularproject.excelformation import *
from modularproject.creatfolder import *
app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')



@app.route('/thrillophilia/activities', methods =['POST','GET'])
@cross_origin()
def deatils():
    search = ['Activity']
    PLACE = ['Place of Activity']
    PRICE = ['Price Per Person']
    RATING = ['Rating']
    VIEWS = ['views on Web Site']
    NAME = ['Visitors Name']
    COMMENT = ['Reviews of visitor']
    PRATING = ['Experience']
    folder_nm = "traveldataexcel"
    urlx=['Webpage link']
    if request.method == 'POST':
        try:
            searchString = request.form['keyword']

            url = 'https://www.thrillophilia.com/tags/' + searchString
            y = uReq(url)
            t = y.read()
            f = bs(t, "html.parser")
            s = f.find_all("span", {"class": "result-card pop-card onclick-link no-select-effects"})

            lst = []

            for i in range(len(s)):
                r = s[i].div.find_next_sibling().a['href']
                url = 'https://www.thrillophilia.com' + r
                y = uReq(url)
                t = y.read()
                f = bs(t, "html.parser")
                e = f.find_all('div', {'class': "review-card"})
                urlx.append(url)
                for i in range(len(e)):

                    try:
                        # cmmnt
                        comment = (e[i].div.find_all('div', {'class': "review-card__review-wrap"})[0].div.text)
                        COMMENT.append(comment)
                    except:
                        comment = "none"

                    try:
                        # name
                        name = (e[i].div.find_all('div', {'class': "review-card__user-name"})[0].text)
                        NAME.append(name)
                    except:
                        name = "none"

                    try:
                        # rating
                        Prating = (e[i].div.div.find_all('div', {'class': "review-card__rating-description"})[0].text)
                        PRATING.append(Prating)
                    except:
                        Prating = "none"

                    try:
                        d = f.find_all('div', {'class': "banner__info-container"})
                        place = (d[0].text.split("\n")[1])
                        PLACE.append(place)
                    except:
                        place = "none"
                    try:
                        rating = (float(d[0].text.split("\n")[3].split("/")[0]))
                        RATING.append(rating)
                    except:
                        rating = "none"
                    try:
                        days = (d[0].text.split("\n")[4])
                        DAYS.append(days)
                    except:
                        days = "none"
                    try:
                        city = (d[0].text.split("\n")[6])
                        CITY.append(city)
                    except:
                        city = "none"
                    try:
                        views = (int(d[0].text.split("\n")[3].split("/")[1].split("(")[1].split(" ")[0]))
                        VIEWS.append(views)
                    except:
                        views = "none"
                    try:
                        d = f.find_all('div', {'class': "pricing-wrap__current-price"})
                        k = (d[0].text.split(" ")[1].split("p")[0]).replace(",", "")
                        m = k + "₹"
                        price = m  # price
                        PRICE.append(price)
                    except:
                        price = "none"
                    search.append((searchString))
                    try:
                        mydict = {"searchString": searchString, "place": place, "price": price, "rating": rating,
                                  "views": views, "name": name, "days": days, "comment": comment, "Prating": Prating}
                        lst.append(mydict)
                    except Exception as e:
                        print("somthing is wronge", e)

            zpped_lists = zip(search, PLACE, PRICE, RATING, VIEWS, NAME, PRATING, urlx, COMMENT)
            keyword = searchString
            autofolder_creation(folder_nm)
            creatExcel(zpped_lists, folder_nm, keyword)
            return render_template('results.html', lst=lst[0:(len(lst) - 1)])

        except Exception as e:
                print("somthing is wronge", e)

if __name__ =="__main__":
    app.run(debug = True)











