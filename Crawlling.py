import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# 여기까지가 크롤링 기본 코딩!!

# request로 우리가 원하는 페이지를 요청하고 bs로 솎아내는 것이 크롤링의 원리이다.

title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

print(title['href'])  # 딱 한 즐만 가지고 오는 것.

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(3)  <---- nth-child() 부분이 달라지는 것을 볼 수 있다.
#old_content > table > tbody > tr

trs = soup.select('#old_content > table > tbody > tr')
#old_content > table > tbody > tr:nth-child(2) >

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    b_tag = tr.select_one('td.point')
    c_tag = tr.select_one('td:nth-child(1)')
    if a_tag is not None:
        rank =  c_tag.img['alt']
        title = a_tag.text
        point = b_tag.text
        print(rank,title,point)

#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1)
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1)
#old_content > table > tbody > tr:nth-child(2) > td.point


