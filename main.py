#
#   Author: Alessandro Taufer
#   Email: alexander141220@gmail.com
#   Url: https://github.com/AlessandroTaufer
#
from website_downloader import WebsiteDownloader


def main():
    w = WebsiteDownloader("http://www.carlopalermo.net/")
    # print(w.retrive_webpage())
    # print(str(w.inspect_webpage(str(w.retrive_webpage()), ["carlopalermo"])))
    w.retrieve_website()


if __name__ == "__main__":
    main()
