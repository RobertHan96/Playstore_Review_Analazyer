import os
import urllib.request
from pathlib import Path

class FileDownloader() :
    chart_names = ["가장_많이_언급된 단어_TOP5", "최근_평점분포", "평점_비율", "Word_cloud"]

    @classmethod
    def downloadImages(self, image_urls):
        download_folder_path = str(os.path.join(Path.home(), "Downloads"))
        for i in range(len(image_urls)) :
            urllib.request.urlretrieve(image_urls[i], "{}/{}.png".format(download_folder_path, self.chart_names[i]))