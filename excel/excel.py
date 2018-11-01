import json
import xlrd
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1')
row, col = (0, 0)
for col in range(1,25):
    ws.write(row, col, col)
col = 0
for row in range(1, 31):
    ws.write(row, col, row)

row = col  = 0
ws.write(row, col, 'Day\Hour')
wb.save("Table_to_learn.xls")

