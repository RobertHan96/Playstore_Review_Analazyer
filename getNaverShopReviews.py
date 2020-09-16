from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import time
import random
import matplotlib.pyplot as plt

# url = "https://shopping.naver.com/fresh/directfarm/stores/100050850/products/3425727137?NaPm=ct%3Dkf3jez76%7Cci%3Dshoppingwindow%7Ctr%3Dswl%7Chk%3Da3c9ce629539aa9c1be2fd0cd2540b6c454c4263%7Ctrx%3D"
# webpage = requests.get(url)
# soup = BeautifulSoup(webpage.text, "html.parser")
# webpage.close()
#
# comments = soup.findAll("span", {"class": "_2Xe0HVhCew"})
# dates = soup.findAll("span", {"class": "_2Xe0HVhCew"})
# stars = soup.findAll("em", {"class": "_3OSAu2awIN"})
# reviews = soup.findAll("div", {"class": "_2B-RlWYmaK"})

test = '2020년 9월 3일'
t1 = test.split(' ')
t2 = t1[2]
t3 = ''
if len(t2) == 3 :
    t3 = t2[:2]
else :
    t3 = t2[:1]

print(t3)