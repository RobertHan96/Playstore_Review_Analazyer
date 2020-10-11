from flask import Flask, render_template, request, redirect, url_for
from Review import Reviews
from ChartsMaker import ChartsMaker
from konlpy.tag import Okt
from collections import Counter
import operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc

app = Flask(__name__)
okt = Okt()

# request_url_for_kartrider = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"
request_url = "https://play.google.com/store/apps/details?id=com.devsisters.gb&showAllReviews=true"

def _main():
    charts_maker = ChartsMaker()
    ratings = []
    dates = []
    nouns_list = []
    review = Reviews(request_url)
    review.getReviews(review.url)

    for i in review.reviews:
        ratings.append(i.stars)
        dates.append(parseReviewDay(i.date))
        noun = okt.nouns(i.comment)  # 명사만 뽑는 함수
        for nn in noun:
            if len(nn) > 1:
                nouns_list.append(nn)

    # 단어만 나열된 하나의 리스트를 가장 많이 언급된 TOP5 단어, 언급횟수 리스트 두개로 변환해서 반환하는 함수
    nouns, nouns_count = sortCounterArrary(nouns_list)

    nouns_counter_dict = Counter(nouns_list)
    ratings, rating_count = sortCounterArrary(ratings)

    # 단어, 언급횟수 or 별점, 별점개수로만 이뤄진 리스트를 통해 챠트 시각화
    charts_maker.wordsFrequencyChart(nouns, nouns_count)
    charts_maker.ratingChart(ratings, rating_count)
    charts_maker.ratingPieChart(rating_count, ratings)

    # 워드크라우드는 단어, 언급횟수가 함께있는 딕셔너리 전
    makeWordCloud(nouns_counter_dict)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form["target_url"]
        # 데이터 크롤링 ~ 분석, 시각화 함수 호출
        # 분석 결과 이미지 파일을 서버에서 다운로드 후 결과페이지로 redirect
        return redirect(url_for("analyze", target_url=url))
    else:
        return render_template('index.html')

@app.route("/analyze", methods=['POST', 'GET'])
def analyze():
    url = request.form.get('target_url')
    return render_template("analyze_result.html", target_url=url)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port='5050')
    _main()

def makeWordCloud(words):
    rc('font', family='NanumBarunGothic')
    # 워드크라우드 디자인 테마 초기 설정
    wc = WordCloud(font_path='/Library/Fonts/NanumBarunGothic.ttf', background_color='white', colormap='Accent_r',
                   width=900, height=400)
    wc.generate_from_frequencies(words)  # 워드크라우드 분석할 데이터를 객체에 삽입
    wc_arrary = wc.to_array()

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wc_arrary, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    fig.savefig('anlytics_result.png')


def sortCounterArrary(arr):
    # 단어만 나열된 하나의 리스트를 가장 많이 언급된 TOP5 단어, 언급횟수 리스트 두개로 변환해서 반환하는 함수
    nouns_result = Counter(arr)
    nouns_result = sorted(nouns_result.items(), key=operator.itemgetter(1), reverse=True)
    frequently_mentioned_words = [i[0] for i in nouns_result[:5]]
    mentioned_time = [i[1] for i in nouns_result[:5]]

    return frequently_mentioned_words, mentioned_time

def convertRatingsForMakeChart(arr):
    # 평점별 개수(5점 ~ 1점 순으로) 리스트 재정렬
    counter_arr = Counter(arr)
    counter_arr = sorted(counter_arr.items(), key=operator.itemgetter(0), reverse=True)
    ratins = [i[0] for i in counter_arr]
    mentioned_time = [i[1] for i in counter_arr]

    return ratins, mentioned_time


def parseReviewDay(review_date):
    # 크롤링시 날짜를 제대로 긁어오도록 파싱하는 함
    day = review_date.split(' ')[2]
    if len(day) == 3:
        day = day[:2]
    else:
        day = day[:1]
    return int(day)
