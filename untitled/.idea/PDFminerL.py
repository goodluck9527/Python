# -*- coding: utf-8 -*-     
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os


def pdf_to_txt(path):
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    if not document.is_extractable():
        raise PDFPageAggregator
    else:
        rsrcmgr = PDFResourceManager()
        device = PDFDevice(rsrcmgr)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(path[:-4]+'.txt', 'a') as f:
                        f.write(x.get_text().encode('utf-8') + '\n')

def main():
    # pdf_to_txt('4.pdf')

    path = '4.pdf'
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    print 'parser: ', parser, '\ndocument: ', document
    # print help(PDFPage)
    rsrcmgr = PDFResourceManager()
    # print rsrcmgr
    device = PDFDevice(rsrcmgr)
    # print device
    inter = PDFPageInterpreter(rsrcmgr, device)
    # print inter
    pages = PDFPage.create_pages(document)
    # print pages
    for page in pages:
        inter.process_page(page)


    # pdf_to_txt('4.pdf')


main()