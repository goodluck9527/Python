import requests
from bs4 import BeautifulSoup

def download(url):
    r = requests.get(url)
    html = r.text

    return html


def read_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


# def main():
#     url = "http://www.baidu.com"
#     html = download(url)
#     soup = read_html(html)
#     # print all the parents of tag <a></a>
#     # iterate the tag tree
#     # print("All the parents of <a>:")
#     # for parent in soup.a.parents:
#     #     if parent is None:
#     #         print(parent)
#     #     else:
#     #         print(parent.name)
#     #
#     # # print all the child of the tag <body></body>
#     # print("All the children of <body>:")
#     # for child in soup.body.children:
#     #     if child is None:
#     #         print(child)
#     #     else:
#     #         print(child.name)
#     #
#     # #print the tag tree sibling and sibling
#     # for sibling in soup.a.next_siblings:
#     #     print(sibling)
#     #
#     # for sibling in soup.a.previous_siblings:
#     #     print(sibling)
#
#     # print the html page with more friendly ways:
#     # use the funtion called prettify in bs4
#     print("Print the page with more friendly ways")
#     print(soup.prettify())
#
#
#
# main()



