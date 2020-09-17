from  Review import Reviews
from konlpy.tag import Okt
from collections import Counter
import  operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc
okt = Okt()
request_url = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"


def convertMentionedWordsForMakeChart(arr) :
    nouns_result = Counter(arr)
    # 단어 등장 횟수가 많은 순서대로 리스트 재정렬
    nouns_result = sorted(nouns_result.items(), key=operator.itemgetter(1), reverse=True)
    frequently_mentioned_words = [i[0] for i in nouns_result[:5]]
    mentioned_time = [i[1] for i in nouns_result[:5]]

    return frequently_mentioned_words, mentioned_time

def convertRatingsForMakeChart(arr) :
    counter_arr = Counter(arr)
    # 평점별 개수(5점 ~ 1점 순으로) 리스트 재정렬
    counter_arr = sorted(counter_arr.items(), key=operator.itemgetter(0), reverse=True)
    ratins = [i[0] for i in counter_arr]
    mentioned_time = [i[1] for i in counter_arr]

    return ratins, mentioned_time
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
        plt.xlabel('단어')
        plt.ylabel('언급 횟수')
        plt.plot(words, mentioned_time, 'skyblue', marker='o', ms=15, mfc='r')
        for x, y in zip(words, mentioned_time):
            label = y
            plt.annotate(label,  # this is the text
                         (x, y),  # this is the point to label
                         va='center',
                         ha='center')  # horizontal alignment can be left, right or center
        plt.show()

    @staticmethod
    def ratingChart(ratings, rating_counts) :
        plt.rc('font', family='NanumBarunGothic')
        plt.title('평점 추이')
        plt.xlabel('평점')
        plt.ylabel('평점 수')
        plt.bar(ratings, rating_counts, color='lightblue')
        plt.show()

    @staticmethod
    def trendsPieChart(positive, negative):
        feedbacks = [positive, negative]
        label = ['긍정', '부정']
        color = ['#14CCC0', '#FF1C6A']
        plt.pie(feedbacks, labels=label, colors=color, autopct='%1.f%%')
        plt.axis('equal')
        plt.show()

    @staticmethod
    def ratingPieChart(rating_count, labels_arr):
        labels = ['{}점'.format(i) for i in labels_arr]
        plt.title('평점 비율')
        plt.pie(rating_count, labels=labels, autopct='%1.f%%')
        plt.axis('equal')
        plt.show()


def makeWordCloud(words) :
    rc('font', family='NanumBarunGothic')
    # 워드크라우드 디자인 테마 초기 설정
    wc = WordCloud(font_path= '/Library/Fonts/NanumBarunGothic.ttf', background_color='white', colormap='Accent_r', width=800, height=800)
    wc.generate_from_frequencies(words) # 워드크라우드 분석할 데이터를 객체에 삽입
    wc_arrary = wc.to_array()

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wc_arrary, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    fig.savefig('anlytics_result.png')

def _main() :
    charts_maker = ChartsMaker()
    ratings = []
    dates = []
    nouns_list = []
    morphs_list = []
    review = Reviews(request_url)
    review.getReviews(review.url)

    for i in review.reviews :
        ratings.append(i.stars)
        dates.append(parseReviewDay(i.date))
        noun = okt.nouns(i.comment) #명사만 뽑는 함수
        morph = okt.morphs(i.comment) #형태소로 구분해서 뽑는 함수
        for nn in noun :
            if len(nn) > 1:
                nouns_list.append(nn)
        for mor in morph :
            morphs_list.append(mor)

    nouns, nouns_count = convertMentionedWordsForMakeChart(nouns_list)
    morphs, morphs_count = convertMentionedWordsForMakeChart(morphs_list)
    nouns_counter_dict = Counter(nouns_list)
    ratings, rating_count = convertMentionedWordsForMakeChart(ratings)

    charts_maker.wordsFrequencyChart(nouns, nouns_count )
    charts_maker.ratingChart(ratings, rating_count)
    charts_maker.ratingPieChart(rating_count, ratings)
    makeWordCloud(nouns_counter_dict)

if __name__ == "__main__":
    _main()
