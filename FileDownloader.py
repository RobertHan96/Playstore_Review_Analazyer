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
        image_file_names = []

        for i in range(len(self.chart_names)) :
            image_file_name = "{}{}_{}.png".format(self.bucket_name, image_name, self.image_url_names[i]).strip()
            image_file_names.append(image_file_name)
        for i in range(len(image_file_names)) :
            download_file_name = "{}/{}.png".format(download_folder_path, self.chart_names[i])
            print("download", image_file_names[i], download_file_name)
            urllib.request.urlretrieve(image_file_names[i], download_file_name)

# https://analyzed-images-bucket.s3.amazonaws.com/627ed98a-f2c0-4fae-bc3e-4e27de6c5834_word_cloud.png
name1 = "https://analyzed-images-bucket.s3.amazonaws.com/627ed98a-f2c0-4fae-bc3e-4e27de6c5834_word_cloud.png"
path = "/Users/mac/Downloads/test_image.png"
name2 = "627ed98a-f2c0-4fae-bc3e-4e27de6c5834_rating_bar_chart.png"
name3 = "627ed98a-f2c0-4fae-bc3e-4e27de6c5834_rating_pie_chart.png"
name4 = "627ed98a-f2c0-4fae-bc3e-4e27de6c5834_word_cloud.png"
urllib.request.urlretrieve(name1, path)
