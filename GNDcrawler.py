# -*- coding: utf-8 -*-
# 바로 윗줄은 한글깨짐, 인코딩 문제를 해결하는 기능성 주석
from urllib.request import urlopen, Request
import urllib
import bs4
import webbrowser
import datetime
import os


# 이 Python 파일 위치
print ("Info : 현재 이 py의 파일 위치")
print (os.getcwd()) #현재 디렉토리의
print (os.path.realpath(__file__))#파일
print (os.path.dirname(os.path.realpath(__file__)) )#파일이 위치한 디렉토리
print ("")


# 코드간 처리시간 측정 함수
def diff_time_function(begin, end):
    diff = end - begin
    elapsed_ms = (diff.days * 86400) + diff.seconds + (diff.microseconds / 1000000)
    return elapsed_ms

    # 측정 마무리 함수
def final_time_print_function():
    return print("--------------------", diff_time_function(process_time, datetime.datetime.now()), "seconds",
                 "----------------------------", diff_time_function(begintime, datetime.datetime.now()), "seconds")


# Text Color Changer
def titleandurl(title, url):
    return print('    ', title, '\n                                                         ', url)



# 통합검색어 입력 및 파싱
source = input('구글, 네이버, 다음 통합검색어를 입력하세요: ')    # 한글로 작성시 에러 뜨는 이슈 보류
print("Info : source의 타입은 : ", type(source))



# 처리 시간 측정 시작 & 각 구간 표시 print
begintime = datetime.datetime.now()
process_time = datetime.datetime.now()
final_time_print_function()


# 각 검색 url 맞춤
process_time = datetime.datetime.now()
urlg = 'https://www.google.co.kr/search?num=10&hl=ko&source=hp&ei=bSM8XMHqNJTX-Qbtub7IBw&q='+ source                # Google은 통합 검색
urln = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='+ source                                 # Naver는 블로그 글 검색
urld = 'https://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&q='+ source                            # Daum도 블로그 글 검색
print("System : url + input \n Google(" + urlg + ") \n Naver(" + urln + ") \n Daum(" + urld + ")")
final_time_print_function()


# Request & etc Setting
process_time = datetime.datetime.now()
    # Google
reqg = urllib.request.Request(urlg, headers={'User-Agent': 'Mozilla/50.0'})     # User-Agent는 Security 관련인데 추후에 찾아볼 것
pageg = urlopen(reqg)
htmlg = pageg.read()
soupg = bs4.BeautifulSoup(htmlg, 'lxml')
print("System : Google soup ready")
final_time_print_function()

    # Naver
process_time = datetime.datetime.now()
reqn = urllib.request.Request(urln, headers={'User-Agent': 'Mozilla/50.0'})
pagen = urlopen(reqn)
htmln = pagen.read()
soupn = bs4.BeautifulSoup(htmln, 'lxml')
print("System : Naver soup ready")
final_time_print_function()

    # Daum
process_time = datetime.datetime.now()
reqd = urllib.request.Request(urld, headers={'User-Agent': 'Mozilla/50.0'})
paged = urlopen(reqd)
htmld = paged.read()
soupd = bs4.BeautifulSoup(htmld, 'lxml')
print("System : Daum soup ready")
final_time_print_function()


# Soup Control

print("Google----------------------------------------------------------------------------")
process_time = datetime.datetime.now()
try :
    link = soupg.select('h3 > a')                                       # Google
    link2 = soupg.select('div > cite')
    for num in range(len(link)) :
         titleandurl(link[num].get_text('h3'), link2[num].get_text('cite'))
except : print('System : Nothing Searched')
final_time_print_function()

print("\nNaver-----------------------------------------------------------------------------")
process_time = datetime.datetime.now()
try :
    link = soupn.find('ul', id='elThumbnailResultArea')                 # Naver
    for link2 in link.find_all('a', class_='sh_blog_title _sp_each_url _sp_each_title') :   
        titleandurl(link2.text.strip(), link2.get('href'))
except : print('System : Nothing Searched')
final_time_print_function()

print("\nDaum------------------------------------------------------------------------------")
process_time = datetime.datetime.now()
try :
    for link2 in soupd.find_all('a', class_='f_link_b'):                # Daum
        titleandurl(link2.get_text(''), link2.get('href')) 
except : print('System : Nothing Searched')

final_time_print_function()



# Open Browser in Chrome
##process_time = datetime.datetime.now()
##chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
##webbrowser.get(chrome_path).open(urlg)
##print("path : " + chrome_path)
##final_time_print_function()



Totaltime = datetime.datetime.now() - begintime
print("------------------Total Processing Time is ------------------" , Totaltime)

