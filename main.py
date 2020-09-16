from  Review import Reviews
from konlpy.tag import Okt
from collections import Counter
import  operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc
okt = Okt()
request_url = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"

def _main() :
    ratings = []
    dates = []
    nouns_list = []
    morphs_list = []
    review = Reviews(request_url)
    review.getReviews(review.url)
    for i in review.reviews :
        ratings.append(i.stars)
        dates.append(par(i.date))
        noun = okt.nouns(i.comment) #명사만 뽑는 함수
        morph = okt.morphs(i.comment) #형태소로 구분해서 뽑는 함수
        for nn in noun :
            if len(nn) > 1:
                nouns_list.append(nn)
        for mor in morph :
            morphs_list.append(mor)

    x, y = m

    ratings = Counter(ratings)
    dates = Counter(dates)
    review_trend_arr = sorted(ratings.items(), key=operator.itemgetter(0), reverse=True)
    dates_arr = [i[0] for i in review_trend_arr]
    ratings_count_arr = [i[1] for i in review_trend_arr]


    # 출현 횟수와 각 단어를 묶어서 딕셔너리 형태로 변환
    # nouns = dict(noun_result.most_common())
    # morphs = dict(morph_result.most_common())

    # 감정분석 사전에서 단어를 분석하고(모듈 import에러 해결 필요)
    # 전체 감정에서 긍정, 부정 비율을 구해서 각각 return
    # 해당 값을 토대로 파이 챠트 생성

    charts_maker = ChartsMaker()
    charts_maker.wordsFrequencyChart(, )
    # charts_maker.trendsPieChart(20, ratings)
    # charts_maker.wordsFrequencyChart(dates, ratings)

def makeNounsArr(arr) :
    nouns_result = Counter(nouns_list)
    # 단어 등장 횟수가 많은 순서대로 리스트 재정렬
    nouns_result = sorted(nouns_result.items(), key=operator.itemgetter(1), reverse=True)
    frequently_mentioned_words = [i[0] for i in nouns_result[:5]]
    mentioned_time = [i[1] for i in nouns_result[:5]]

    return frequently_mentioned_words, mentioned_time

def parseReviewDay(review_date) :
    day = review_date.split(' ')[2]
    if len(day) == 3:
        day = day[:2]
    else :
        day = day[:1]
    return int(day)


class ChartsMaker :
    @staticmethod
    def wordsFrequencyChart(words, mentioned_time) :
        plt.rc('font', family='NanumBarunGothic')
        plt.title('가장 많이 언급된 단어')
        plt.plot(words, mentioned_time, 'skyblue')
        plt.show()

    @staticmethod
    def ratingChart(date, stars) :
        plt.rc('font', family='NanumBarunGothic')
        plt.title('평점 추이')
        plt.plot(stars, date, 'skyblue')
        plt.show()

    @staticmethod
    def trendsPieChart(positive, negative):
        feedbacks = [positive, negative]
        label = ['긍정', '부정']
        color = ['#14CCC0', '#FF1C6A']
        plt.pie(feedbacks, labels=label, colors=color, autopct='%1.f%%')
        plt.axis('equal')
        plt.show()


class WordCloud :
    def makeWordCloud(words) :
        rc('font', family='NanumBarunGothic')
        # 워드크라우드 디자인 테마 초기 설정
        wc = WordCloud(font_path= '/Library/Fonts/NanumBarunGothic.ttf', background_color='white', colormap='Accent_r', width=800, height=800)
        wc.generate_from_frequencies(words) # 워드크라우드 분석할 데이터를 객체에 삽입
        # wc_arrary = wc.to_array()

        # return wc_arrary

    def makeWordCloudImageFile(wc_arr):
        fig = plt.figure(figsize=(10, 10))
        plt.imshow(wc_arr, interpolation="bilinear")
        plt.axis('off')
        plt.show()
        fig.savefig('anlytics_result.png')

if __name__ == "__main__":
    _main()
