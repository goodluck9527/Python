import json
import xlwt

def getJson(path):
    file = open(path, 'r')
    return json.load(file)

def writeExcel(header, v):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')
    # for c in range(len(header)):
    #     ws.write(0, c, header[c])
    #     for r in range(len(v)):
    #         ws.write(r+1, c, v[r][header[c]])
    # wb.save('tesss.xls')

    dictionary = {}
    for i in range(1, len(j) + 1):
        length = len(j[i])
        if length > 1:
            for r in range(1, length ):
                dictionary[str(j[i][r])] = header.index(str(j[i][r]))

    col, row = (0 ,0)
    for col in range(len(header)):
        ws.write(row, col, header[col])

    col = 0
    for row in range(len(v)):
        ws.write(row + 1, col, v[row][0])
        for i in range(v[row] - 1):
            ws.write(row + 1, i + 1, )

    wb.save('asdfasdf.xls')

header = ['IP', '80:web','8080:web','3311:kangle','3312:kangle','3389:mstsc','4440:rundeck','5672:rabbitMQ','5900:vnc','6082:varnish','7001:weblogic','8161:activeMQ','8649:ganglia','000:fastcgi','9090:ibm','9200:elasticsearch','9300:elasticsearch','9999:amg','10050:zabbix','11211:memcache','27017:mongodb','28017:mondodb','3777:dahua jiankong','50000:sap netweaver','50060:hadoop','50070:hadoop','21:ftp','22:ssh','23:telnet','25:smtp','53:dns','123:ntp','161:snmp','8161:snmp','162:snmp','389:ldap','443:ssl','512:rlogin','513:rlogin','73:rsync','433:mssql','1080:socks','1521:oracle','1900:bes','2049:nfs','2601:zebra','2604:zebra','2082:cpanle','2083:cpanle','3128:squid','3312:squid','3306:mysql','4899:radmin','834:nessus','45:microsoft-ds','135:msrpc']
#
# writeExcel(header, getJson('open_ports_data.jso)n')

j = getJson('open_ports_data.json')
# for i in range(100):
#     print("{}th: ip: {}".format(i, j[i]))
for i in j:
    
writeExcel(header, j)
