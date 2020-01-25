#
#   Author: Alessandro Taufer
#   Email: alexander141220@gmail.com
#   Url: https://github.com/AlessandroTaufer
#
import urllib.request
import urllib.error
import urllib.parse

# url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
#
# response = urllib.request.urlopen(url)
# webContent = response.read()
#
# print(webContent[0:300])
import logging


class WebsiteDownloader:

    def __init__(self, url_root = "", folder=None):
        if folder is None:
            folder = "resources/"

        self.default_folder = folder
        self.url = url_root
        self.urls_crawled = []  # List of all the urls that has been crawled

    def retrieve_website(self, url=None):
        if url is None:
            url = self.url
        remaining_urls = [url]
        for u in remaining_urls:
            print("Currently inspecting: " + u)  # TODO use logging library
            webpage_urls = self.inspect_webpage(str(self.retrive_webpage(u)), [self.url])
            self.urls_crawled.append(u)
            if webpage_urls is None:
                continue
            for wu in webpage_urls:
                if wu not in self.urls_crawled and wu not in remaining_urls:
                    remaining_urls.append(wu)
        return self.urls_crawled

    def retrive_webpage(self, url=None, save_on_file=True):  # Retrieve webpage content
        if url is None:
            url = self.url
        try:
            response = urllib.request.urlopen(url)
            content = response.read()
        except urllib.error.HTTPError:
            print("Failed to inspect: " + url)
            return

        if save_on_file:
            path = url.replace(self.url, "")
            if path == "":
                path = "index"
            if path[-1] == "/":
                tmp = list(path)
                tmp[-1] = ""
                path = "".join(path)
            path = path.replace("/", "-")

            path = self.default_folder + path + ".html"
            self.write_to_file(content, path)
        self.urls_crawled.append(url)
        return content

    @staticmethod
    def inspect_webpage(content, filter=None):  # Inspect the webpage looking for links (related to the main url)
        content = content.replace("\'", "\"")
        tmp = content.split("href")
        verified_urls = []
        for i in range(1, len(tmp)-1):
            url = tmp[i].split("\"")[1]
            cache_url = False
            if filter is not None:
                for f in filter:
                    if f in url:
                        cache_url = True

            else:
                cache_url = True

            if cache_url:
                verified_urls.append(url)
        return verified_urls

    @staticmethod
    def write_to_file(content, filename):
        with open(filename, "wb") as f:
            f.write(content)
            f.close()
