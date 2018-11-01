import re
import urllib2
import urlparse


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


def link_crawler(seed_url, link_regex):
    """
    Crawl from the given seed URL following links matched by link_regex
    :param seed_url:
    :param link_regex:
    :return:
    """
    print "in link_crawler"
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    """
    :param htmml: a string content all the information of the html file
    :return: a list of links from html
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)

    return webpage_regex.findall(html)


def main():
    link_crawler("http://example.webscraping.com", '/(index|view)')


main()
