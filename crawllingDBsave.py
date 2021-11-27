import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta



trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    b_tag = tr.select_one('td.point')
    c_tag = tr.select_one('td:nth-child(1)')
    if a_tag is not None:
        rank =  c_tag.img['alt']
        title = a_tag.text
        point = b_tag.text
        doc = {'rank':rank,'title':title, 'point':point}

        print(db.movies.insert_one(doc))