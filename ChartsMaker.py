import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import rc
import uuid
import base64
from io import BytesIO

from wordcloud import WordCloud
from AwsManager import AwsManager

def make_uuid():
    uid = str(uuid.uuid4())
    return uid

class ChartsMaker():
    aws = AwsManager(make_uuid())

    @classmethod
    def makeFig(self):
        plt.figure(figsize=(4, 3))
        plt.rc('font', family='NanumBarunGothic')
        plt.title('가장 많이 언급된 단어')
        plt.xlabel('언급된 단어')
        plt.ylabel('언급 횟수')
        plt.plot(['안녕', '하세요','그럼','테슽', '트'], [1,2,3,4,5], 'skyblue', marker='o', ms=15, mfc='r')

        img = BytesIO()
        plt.savefig(img, format='png', dpi=200)
        ## object를 읽었기 때문에 처음으로 돌아가줌
        chart = img.seek(0)
        return chart

    @classmethod
    def wordsFrequencyChart(self, words, mentioned_time):
        fig_path = 'static/images/word_frequency_chart.png'
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
        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path)
        plt.close(fig_path)

    @classmethod
    def ratingChart(self, ratings, rating_counts):
        fig_path = 'static/images/rating_bar_chart.png'
        plt.rc('font', family='NanumBarunGothic')
        plt.title('평점 추이')
        plt.xlabel('평점')
        plt.ylabel('평점 수')
        plt.bar(ratings, rating_counts, color='lightblue')
        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path)
        plt.close(fig_path)

    @classmethod
    def ratingPieChart(self, rating_count, labels_arr):
        fig_path = 'static/images/rating_pie_chart.png'
        labels = ['{}점'.format(i) for i in labels_arr]
        plt.title('평점 비율')
        plt.pie(rating_count, labels=labels, autopct='%1.f%%')
        plt.axis('equal')
        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path)
        plt.close(fig_path)

    @classmethod
    def makeWordCloud(self, words):
        fig_path = 'static/images/word_cloud.png'
        rc('font', family='NanumBarunGothic')
        # 워드크라우드 디자인 테마 초기 설정
        wc = WordCloud(font_path='/Library/Fonts/NanumBarunGothic.ttf', background_color='white', colormap='Accent_r',
                       width=900, height=400)
        wc.generate_from_frequencies(words)  # 워드크라우드 분석할 데이터를 객체에 삽입
        wc_arrary = wc.to_array()

        fig = plt.figure(figsize=(10, 10))
        # plt.imshow(wc_arrary, interpolation="bilinear")
        plt.axis('off')
        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path)


