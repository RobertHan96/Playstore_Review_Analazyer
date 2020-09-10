from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ErrorHanlder :
    crwaling_fail_text = "크롤링 실패"
    connection_fail_err_text = "Error : 타겟 사이트 접속 불가\n"

class Review:
    date = ''
    comment = ''
    stars = 0

    def __init__(self, date, comment, stars):
        self.date = date
        self.comment = comment
        self.stars = stars

class Reviews :
    url = ''
    reviews = []
    timeout_limit = 5
    crwaled_reviews_count = -2

    def __init__(self, url):
        self.url = url

    @classmethod
    def is_requstable(self):
        try:
            urllib.request.urlopen(url=self.url, timeout=self.timeout_limit)
            return True
        except urllib.request.URLError as err:
            print(ErrorHanlder.connection_fail_err_text, err)
            return False

    @classmethod
    def getReviews(self, url):
        try:
            driver_path = "/Users/mac/0_Dev/PythonProjects/analazye_users_feedback/chromedriver"
            driver = webdriver.Chrome(driver_path)
            driver.get(url)
            driver.implicitly_wait(100)

            for i in range(10) :
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)

            html = driver.page_source
            bs = BeautifulSoup(html, "lxml")

            dates =  bs.findAll("span", {"class" : "p2TkOb"})
            comments = bs.findAll("div", {"class" : "UD7Dzf"})
            stars = driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']")
            star_arr = []
            for star in stars :
                self.crwaled_reviews_count += 1
                rated_text = star.get_attribute('aria-label')
                rated_text =  RawHtmlParser.parseStarInfo(rated_text)
                star_arr.append(rated_text)

            for i in range(len(comments)):
                review = Review(dates[i].text, comments[i].text, star_arr[i])
                self.reviews.append(review)

            driver.close()
            driver.quit()
            return self.reviews
        except:
            print(ErrorHanlder.crwaling_fail_text)
            return self.reviews

class RawHtmlParser :
    @staticmethod
    def parseStarInfo(text) :
        rated_scores = ['0','1', '2', '3', '4', '5']
        results = 0
        for tt in text:
            if tt in rated_scores:
                results = int(tt)
        return results
