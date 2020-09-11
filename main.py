from  Review import  Review, Reviews
from konlpy.tag import Okt
from collections import Counter
import  operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc
okt = Okt()
request_url = "https://play.google.com/store/apps/details?id=com.nexon.kart&showAllReviews=true"

def _main() :
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
    # nounArr = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    # 출현 횟수와 각 단어를 묶어서 딕셔너리 형태로 변환
    nouns = dict(noun_result.most_common())
    morphs = dict(noun_result.most_common())
    print(morphs)
    # rc('font', family='NanumBarunGothic')
    # wc = WordCloud(font_path= '/Library/Fonts/NanumBarunGothic.ttf',background_color='white', colormap='Accent_r', width=800, height=800)
    # wordcloud_words = wc.generate_from_frequencies(words)
    # array = wc.to_array()
    # print(type(array)) # numpy.ndarray
    # print(array.shape) # (800, 800, 3)
    #
    # fig = plt.figure(figsize=(10, 10))
    # plt.imshow(array, interpolation="bilinear")
    # plt.axis('off')
    # plt.show()
    # fig.savefig('business_anlytics_worldcloud.png')

def makeWordCloud(words) :
    pass

if __name__ == "__main__":
    _main()
