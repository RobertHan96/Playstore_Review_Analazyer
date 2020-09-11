from  Review import  Review, Reviews
from konlpy.tag import Okt
from collections import Counter
import sys
import  operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc
okt = Okt()
request_url = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"


def _main() :
    wc = WordCloud()
    nouns_list = []
    morphs_list = []
    review = Reviews(request_url)
    review.getReviews(review.url)
    for i in review.reviews :
        noun = okt.nouns(i.comment) #명사만 뽑는 함수
        morph = okt.morphs(i.comment) #형태소로 구분해서 뽑는 함수
        for nn in noun :
            if len(nn) > 1:
                nouns_list.append(nn)
        for mor in morph :
            morphs_list.append(mor)
    # 각 단어별 출현 횟수 카운팅
    noun_result = Counter(nouns_list)
    morph_result = Counter(morphs_list)
    morph_arr = sorted(morph_result.items(), key=operator.itemgetter(1), reverse=True)
    morph_arr = morph_arr[:5]
    frequently_mentioned_words = [i[0] for i in morph_arr]
    mentioned_time = [i[1] for i in morph_arr]

    # 출현 횟수와 각 단어를 묶어서 딕셔너리 형태로 변환
    # nouns = dict(noun_result.most_common())
    # morphs = dict(morph_result.most_common())
    plt.rc('font', family='NanumBarunGothic')
    plt.title('가장 많이 언급된 단어')
    plt.plot(frequently_mentioned_words, mentioned_time,'skyblue')
    plt.show()

    label = ['긍정', '부정']
    color = ['#14CCC0', '#389993',
    plt.pie(, labels=label, colors=color, autopct='%1.f%%')
    plt.axis('equal')


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
