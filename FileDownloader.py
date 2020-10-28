import os
import urllib.request
from pathlib import Path

class FileDownloader() :
    chart_names = ["가장_많이_언급된 단어_TOP5", "최근_평점분포", "평점_비율", "Word_cloud"]
    image_url_names = ["word_frequency_chart", "rating_bar_chart", "rating_pie_chart", "word_cloud"]
    bucket_name = "https://analyzed-images-bucket.s3.amazonaws.com/"

    @classmethod
    def downloadImages(self, image_name):
        download_folder_path = str(os.path.join(Path.home(), "Downloads"))
        image_urls = []

        for i in range(len(self.chart_names)) :
            image_urls.append("{}{}_{}.png".format(self.bucket_name, image_name, self.image_url_names[i]).strip())
        for i in range(len(image_urls)) :
            urllib.request.urlretrieve(image_urls[i], "{}/{}.png".format(download_folder_path, self.chart_names[i]))
