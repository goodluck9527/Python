import urllib2
import re


def download(url):
    print "Downloading: ", url
    html = urllib2.urlopen(url).read()

    return html


def main():
    url_seed = "http://riper-ma.github.io"
    html = download(url_seed)
    links = re.findall("<a(.*?)href=\"/(.*?)/\"", html)
    li = []
    riper = []
    i = 0

    for link in links:
        i += 1
        tmp = url_seed + '/' + link[-1] + '/'
        li.append(tmp)
        f = open(str(i) + ".html", "w")
        f.write(download(tmp))
        riper.append(f)


main()
