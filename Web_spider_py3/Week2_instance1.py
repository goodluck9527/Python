from bs4 import BeautifulSoup
import spider_with_bs4

def instance1(url):
    html = spider_with_bs4.download(url)
    soup = spider_with_bs4.read_html(html)
    links = []

    for link in soup.find_all('a'):
        link.append(link)
        print(link)

    return links


def main():
    url = "http://baidu.com"
    instance1(url)

main()
