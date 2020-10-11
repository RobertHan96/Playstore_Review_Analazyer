import urllib.request

class ImageDownloader :
    @staticmethod
    def imageDownload():
        url = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcBMAPp%2FbtqEHPlyuTt%2FMJ6UjEuzPqJtXGlGODdMoK%2Fimg.png"
        download_path = "/Users/mac/0_Dev/PythonProjects/analazye_users_feedback/static/Images/test.png"
        # 이미지 요청 및 다운로드
        urllib.request.urlretrieve(url, download_path)


