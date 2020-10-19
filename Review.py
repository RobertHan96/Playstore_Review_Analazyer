from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
import asyncio

# ErrorHanlder : 크롤링 도중 예외 발생시 보여줄 콘솔 안내문구를 모아놓은 데이터 클래스
class ErrorHanlder :
    crwaling_fail_text = "크롤링 실패"
    crwaling_completed_text = "크롤링 완료"
    connection_fail_err_text = "Error : 타겟 사이트 접속 불가\n"

# Review : 각각의 리뷰 정보 저장 객체 : date(리뷰 날짜), comment(리뷰 내용), stars(평점)
class Review:
    date = ''
    comment = ''
    stars = 0

    def __init__(self, date, comment, stars):
        self.date = date
        self.comment = comment
        self.stars = stars

# 크롤링 로직 & 크롤링 결과 리스트를 담고 있는 객체
class Reviews :
    url = ''
    reviews = []

    # timeout_limit : 해당 시간(초)내로 target_url에 응답이 없으면, 네트워크 연결이 없다고 간주하고 크롤링 중단
    timeout_limit = 5
    crwaled_reviews_count = -2

    def __init__(self, url):
        self.url = url

    # is_requstable : url 접속여부를 통해서 크롤링 가능 여부 확인
    @classmethod
    def is_requstable(self):
        try:
            urllib.request.urlopen(url=self.url, timeout=self.timeout_limit)
            return True
        except urllib.request.URLError as err:
            print(ErrorHanlder.connection_fail_err_text, err)
            return False

    # getReviews : 셀레니움을 통해 사이트 접속 & 크롤링
    @classmethod
    def getReviews(self, url):
        try:
            driver_path = "/Users/mac/0_Dev/PythonProjects/review_analazyer/chromedriver"
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
            print(ErrorHanlder.crwaling_completed_text)
            return self.reviews
        except:
            print(ErrorHanlder.crwaling_fail_text)
            return self.reviews

# html의 평점 데이터를 크롤링하기 까다로워서 별도의 클래스=>함수로 구현
class RawHtmlParser :
    @staticmethod
    def parseStarInfo(text) :
        rated_scores = ['0','1', '2', '3', '4', '5']
        results = 0
        for tt in text:
            if tt in rated_scores:
                results = int(tt)
        return results
