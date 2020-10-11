from collections import Counter
import operator

class ReviewDataParser :

    @staticmethod
    def sortCounterArrary(arr):
        # 단어만 나열된 하나의 리스트를 가장 많이 언급된 TOP5 단어, 언급횟수 리스트 두개로 변환해서 반환하는 함수
        nouns_result = Counter(arr)
        nouns_result = sorted(nouns_result.items(), key=operator.itemgetter(1), reverse=True)
        frequently_mentioned_words = [i[0] for i in nouns_result[:5]]
        mentioned_time = [i[1] for i in nouns_result[:5]]

        return frequently_mentioned_words, mentioned_time

    @staticmethod
    def convertRatingsForMakeChart(arr):
        # 평점별 개수(5점 ~ 1점 순으로) 리스트 재정렬
        counter_arr = Counter(arr)
        counter_arr = sorted(counter_arr.items(), key=operator.itemgetter(0), reverse=True)
        ratins = [i[0] for i in counter_arr]
        mentioned_time = [i[1] for i in counter_arr]

        return ratins, mentioned_time

    @staticmethod
    def parseReviewDay(review_date):
        # 크롤링시 날짜를 제대로 긁어오도록 파싱하는 함
        day = review_date.split(' ')[2]
        if len(day) == 3:
            day = day[:2]
        else:
            day = day[:1]
        return int(day)
