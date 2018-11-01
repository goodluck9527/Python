import os

for root,dirs,files in os.walk(r"F:\program files\python\untitled\.idea"):
    for file in files:
        pdf = "'" + os.path.join(root,file).decode('gbk').encode('utf-8') + "'";
        pdfs = pdf.replace('\\','\\\\')
        txt = pdf.replace('pdf','txt')
        print pdfs
        # # print txt
        # # f = open(txt,'w')
        fp = open(pdfs,'rb')
        fp.close()