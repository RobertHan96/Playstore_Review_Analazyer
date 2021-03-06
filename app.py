# 사용자 정의 클래스 3개 import 필요
# - Reviews : 플레이스토어 데이터 크롤링 모듈
# - ReviewDataParser : 크롤링된 리스트를 데이터 시각화하기 좋은 형태로 파싱하는 모듈
# - ChartsMaker : 그래프, 워드크라우드 제작 모듈

from Review import Reviews
from ReviewDataParser import  ReviewDataParser
from ChartsMaker import ChartsMaker


from flask import Flask, render_template, request, redirect, url_for
# - konlpy : 유저가 남긴 리뷰 문장을 단어 단위로 분석해서 나눠주는 용도
    # 의존성 주입 : pip install konlpy
from konlpy.tag import Okt
# - collections : 리스트내에 특정 데이터가 들어간 횟수를 count해서 딕셔너리로 바꿔주는 용도
    # 의존성 주입 : 파이썬 기본 라이브러리, 그냥 import 가능
from collections import Counter

app = Flask(__name__)
okt = Okt()

# 유저동향을 분석할 사이트 주소 (크롤링할 주소가 됨)
request_url = "https://play.google.com/store/apps/details?id=com.devsisters.gb&showAllReviews=true"

def _main():
    # 데이터 시각화, 파싱을 위해 만든 모듈을 객체 형태로 불러옴
    charts_maker = ChartsMaker()
    data_parser = ReviewDataParser()

# ratings : 유저들이 메겼던 평점 , dates : 유저가 리뷰를 남긴 날짜
# nouns_list : 유저 리뷰 내용을 konlpy라이브러리로 명사 단어 단위로 나눈 뒤 저장할 리스트
    ratings = []
    dates = []
    nouns_list = []
    # 크롤링할 데이터를 담을 review 객체를 생성하고, getReivew() 함수로 입력받았던 url에 대한 크롤링 시작
    review = Reviews(request_url)
    review.getReviews(review.url)

    # 크롤링이 끝나면 크롤링 완료 or 실패 메세지가 콘솔에 출력
    # 크롤링된 리뷰들이 쌓인 reviews 리스트를 순회하면서 각 리뷰의 (평점, 날짜, 리뷰 내용)을 위에서 선언해놨던 배열들에 각각 추가
    for i in review.reviews:
        ratings.append(i.stars)
        # 날짜는 데이터를 추가하기 전에 포맷을 통일하기 위해 parseReviewDay 함수를 이용해야 함
        # ex) 1~9일, 즉 한 자리로 들어오는 날짜들을 01, 02, 03.. 형태로 변환해줌
        dates.append(data_parser.parseReviewDay(i.date))

        # 명사만 뽑는 함수 okt.nouns를 이용해 string 형태의 리뷰 내용을 단어 단위의 리스트로 변환함
        # Ex) "안녕하세요 오늘 날씨가 좋습니다" => ["안녕", "하세요", "오늘", "날씨", "좋습니다"] 형태의 리스트로 바뀌게 됨
        noun = okt.nouns(i.comment)
        for nn in noun:
            # 각 단어들을 nouns_list에 추가하되, 단어길이가 2글자 이상인 경우만 추가함
            # 단어 길이가 1인 경우(은, 는, 이, 가, 기호) 처럼 의미없는 단어일 확률이 높기 때문
            if len(nn) > 1:
                nouns_list.append(nn)


    # sortCounterArrary : 단어 리스트를 단어, 단어 언급횟수 두개의 리스트로 나눠주는 함수
    # Ex) ['안녕', '안녕', '안녕, '이득', '개이득'] => ['안녕', '이득', '개이득'], [3, 1, 1] 두개의 리스트로 결과값 반환
    # 위 2개의 리스트를 이용해서 많이 언급된 TOP5 단어 그래프를 만들수 있음
    nouns, nouns_count = data_parser.sortCounterArrary(nouns_list)
    ratings, rating_count = data_parser.sortCounterArrary(ratings)

    # 워드크라우드 제작을 위해 기존의 단어리스트를 딕셔너리 형태로 변환
    # Ex) {"게임" : 123, "현질유도": 76, "이벤트" : 22}
    nouns_counter_dict = Counter(nouns_list)

    # 단어, 언급횟수 or 별점, 별점개수로만 이뤄진 리스트를 통해 챠트 시각화
    charts_maker.wordsFrequencyChart(nouns, nouns_count)
    charts_maker.ratingChart(ratings, rating_count)
    charts_maker.ratingPieChart(rating_count, ratings)

    # makeWrodCloud 함수는 {단어 : 언급횟수} 형태의 딕셔너리 값을 넣어서 호출 해야함
    charts_maker.makeWordCloud(nouns_counter_dict)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form["target_url"]
        # POST로 유저가 분석할 url을 입력한 경우에만 데이터 분석 함수를 실행하고, 결과창으로 redirect
        return redirect(url_for("analyze", target_url=url))
    else:
        # 그 외, GET로 요청된 경우 메인 페이지를 보여줌
        return render_template('index.html')

@app.route("/analyze", methods=['POST', 'GET'])
def analyze():
    url = request.form.get('target_url')
    return render_template("analyze_result.html", target_url=url)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port='5050') 플라스크서버 실행용
    _main()