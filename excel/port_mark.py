import json
import xlwt

def getJson(path):
    file = open(path, 'r')
    return json.load(file)

def writeExcel(header, v):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')

    # create a dictionary to save the number of diffrent ports, 
    # and you can use the position to mark the port 
    # Meanwhile, create the header list
    dictionary = {}
    for i in range(1, len(j)):
        length = len(v[i])
        if length > 1:
            for r in range(1, length ):
                string = str(v[i][r])
                if not string in header:
                    header.append(string)
                    dictionary[string] = header.index(string)
                else:
                    dictionary[string] = header.index(string)

    # write header to the excel
    col, row = (0 ,0)
    for col in range(len(header)):
        ws.write(row, col, header[col])


    # mark all with open
    col = 0
    # fill the first line
    for row in range(len(v)):
        # fill value called ip from list[0] in json
        ws.write(row + 1, col, v[row][0])
        for i in range(len(v[row]) - 1):
            string = str(v[row][i+1]);
            # mark all, row + 1 to skip header, i + 1 to skip ip
            print((row+2,string,dictionary[str(v[row][i+1])] ))
            ws.write(row + 1, dictionary[str(v[row][i+1])], 'open')

    wb.save('端口数据开放情况统计.xls')

header = ['IP']
j = getJson('open_ports_data.json')

writeExcel(header, j)