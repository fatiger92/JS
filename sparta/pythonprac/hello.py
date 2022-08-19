
# 변수 선언에 자료형 안 적어도 됨
# a = 2
# b = 3
# c = "Victor"
# d = "Ji"
# print(a+b, c+d);

# 리스트 정의
# a_list = ['사과', '배', '감']
# a_list.append('수박')
# print(a_list)

# for 문과 딕셔너리
# a_dict = {
#     'name' : 'bob',
#     'age': 27
# }
# a_dict['gender'] = "male"
# for key in a_dict:
#     print(key, ':', a_dict[key])

# 함수
# def sum(a,b):
#     print('더하자')
#     return a+b;
#
# result = sum(1,2)
# print(result)

# def is_adult(age):
#     if age > 20:
#         print('성인입니다')
#     else:
#         print('청소년입니다.')
#
# is_adult(25)

# 리스트 예제
# count = 0
#
# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
# for fruit in fruits:
#     if fruit == '배':
#         count += 1
#
# print(count)

# 딕셔너리 예제
# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
#
# for person in people:
#     if person['age'] > 20:
#         print(person['name'])

# requests 패키지 사용
# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()
#
# rows = rjson['RealtimeCityAir']['row']
# for row in rows:
#     gu_name = row['MSRSTE_NM']
#     gu_mise = row['IDEX_MVL']
#     if gu_mise < 60:
#         print(gu_name)

# 크롤링
# bs4(beautifulsoup) package 설치
# headers 를 사용하는 이유는 사람이 웹에 Req를 날린 것 처럼 하기 위해서.
import string
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.s9m5n3l.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title.text)
# print(title['href'])

# old_content > table > tbody > tr:nth-child(3) > td.title > div > a
# old_content > table > tbody > tr:nth-child(4) > td.title > div > a

#old_content > table > tbody > tr:nth-child(2) > td.point

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img

# movies = soup.select('#old_content > table > tbody > tr')
# for movie in movies:
#     a = movie.select_one('td.title > div > a')
#     if a != None:
#         print(a.text)

movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    a = movie.select_one('td.title > div > a')

    if a != None:
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star
        }
        db.movies.insert_one(doc)


