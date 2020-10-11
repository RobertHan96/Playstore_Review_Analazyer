import matplotlib.pyplot as plt
from matplotlib import rc
from wordcloud import WordCloud

class ChartsMaker:
    @staticmethod
    def wordsFrequencyChart(words, mentioned_time):
        plt.rc('font', family='NanumBarunGothic')
        plt.title('가장 많이 언급된 단어')
        plt.xlabel('언급된 단어')
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
    def ratingChart(ratings, rating_counts):
        plt.rc('font', family='NanumBarunGothic')
        plt.title('평점 추이')
        plt.xlabel('평점')
        plt.ylabel('평점 수')
        plt.bar(ratings, rating_counts, color='lightblue')
        plt.show()

    @staticmethod
    def ratingPieChart(rating_count, labels_arr):
        labels = ['{}점'.format(i) for i in labels_arr]
        plt.title('평점 비율')
        plt.pie(rating_count, labels=labels, autopct='%1.f%%')
        plt.axis('equal')
        plt.show()

    @staticmethod
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

