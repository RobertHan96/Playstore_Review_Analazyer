# 유저 동향 분석 웹 앱 
***

# 프로젝트 구성 
- static : 웹페이지용 css, js, 사진, 동영상
- templates : flask 문법이 적용된 Html
    - index.html : 메인 페이지 
    - analyze_result.html : 메인페이지에서 입력한 url에 대한 분석 결과를 보여주는 폐이지
- app.py : 크롤링, 플라스크 서버를 실행하는 메인 시작점
- AwsManager.py : aws인증, s3파일 서버 접속 관련 모듈
- Review.py : 플레이스토어 리뷰 크롤링 모듈
- ChartsMaker : 배열, 딕셔너리 데이터를 시각화하는 모듈
- ReviewDataPaser.py : 크롤링된 텍스트를 시각화하기 좋은 형태로 변환하는 모듈
- venv : 앱 구동에 필요한 라이브러리가 설치된 가상 환경
- chromedriver : 크롬 드라이버 for 크롬 v.86

***