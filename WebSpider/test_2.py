import re
import urllib2
import itertools


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading: ', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download Error!', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    f = open("sitemap.xml", 'w')
    f.write(sitemap)
    links = re.findall('<a href=(.*?)>', sitemap)
    print links
    for link in links:
        link = link[1:-1]
        html = download(link)
        f = open("tmp.html", 'w')
        f.write(html)


def main():
    # crawl_with_sitemap
    url = "http://riper-ma.github.io"
    crawl_sitemap(url)
    # crawl_with_ID
    # for page in itertools.count(1):
    #     url = 'http://example.webscraping.com/view/-%d' % page
    #     html = download(url)
    #     if html is None:
    #         break
    #     else:
    #         print html
    #         pass


main()
