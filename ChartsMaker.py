# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import rc
from User import make_uuid
from io import BytesIO

from wordcloud import WordCloud
from AwsManager import AwsManager

class ChartsMaker():
    aws = AwsManager()
    uid = make_uuid()

    @classmethod
    def make_charts(self, data):
        nouns = data[0]
        nouns_count = data[1]
        ratings = data[2]
        rating_count = data[3]
        nouns_counter_dict = data[4]
        # 단어, 언급횟수 or 별점, 별점개수로만 이뤄진 리스트를 통해 챠트 시각화
        words_frequency_chart = self.wordsFrequencyChart(nouns, nouns_count)
        rating_chart = self.ratingChart(ratings, rating_count)
        rating_pie_chart = self.ratingPieChart(rating_count, ratings)
        # makeWrodCloud 함수는 {단어 : 언급횟수} 형태의 딕셔너리 값을 넣어서 호출 해야함
        wrod_cloud = self.makeWordCloud(nouns_counter_dict)
        byte_images = [words_frequency_chart, rating_chart, rating_pie_chart, wrod_cloud]
        print("all charts are uploaded")
        return byte_images, self.uid

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
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path, self.uid)
        img = BytesIO()
        plt.savefig(img)
        img.seek(0)
        plt.close()
        return img

    @classmethod
    def ratingChart(self, ratings, rating_counts):
        fig_path = 'static/images/rating_bar_chart.png'
        plt.rc('font', family='NanumBarunGothic')
        plt.title('평점 추이')
        plt.xlabel('평점')
        plt.ylabel('평점 수')
        plt.bar(ratings, rating_counts, color='lightblue')

        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path, self.uid)

        img = BytesIO()
        plt.savefig(img)
        img.seek(0)
        plt.close()
        return img

    @classmethod
    def ratingPieChart(self, rating_count, labels_arr):
        fig_path = 'static/images/rating_pie_chart.png'
        labels = ['{}점'.format(i) for i in labels_arr]
        plt.title('평점 비율')
        plt.pie(rating_count, labels=labels, autopct='%1.f%%')
        plt.axis('equal')

        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path, self.uid)

        img = BytesIO()
        plt.savefig(img)
        img.seek(0)
        plt.close()
        return img

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
        plt.imshow(wc_arrary, interpolation="bilinear")
        plt.axis('off')
        plt.savefig(fig_path)
        self.aws.upload_file_to_bucket(self.aws.bucket_name, fig_path, self.uid)

        img = BytesIO()
        plt.savefig(img)
        img.seek(0)
        plt.close()
        return img



