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

# 서버 로직 
- 1) main에서 유저가 form을 통해 분석하고 싶은 Url 입력
- 2) 해당 url에서 크롤링해서 데이터를 가져옴
- 3) 가져온 데이터를 matplotlib을 이용해서 이미지 형태로 챠트 생성
- 4) 생성된 이미지 => aws S3 업로드
- 5) 차트 종류별 이미지를 bytes형태의 리스트로 return 
- 6) analayze_result 페이지 렌더링 호출, 종류별 이미지를 함께 전달
- 7) analayze_result에서 리스트의 각 요소에 접근해서 분석 결과를 이미지 형태로 확인
- 8) 모두 다운로드 버튼 제공 
- 9) uuid기반으로 s3에서 해당 유저가 요청했던 이미지를 검색하고, 모두 다운로드 진행