import xlwt # 写入Excel
import xlrd # 读取Excel

def create():
    # 创建Excel
    Excel_book=xlwt.Workbook()
    # 创建一个sheet
    sheet=Excel_book.add_sheet('test01')
    # 在第一行第一列写入文字‘Python’
    # sheet.write(0,0,'Python')
    t=1
    for i in range(3):
        for j in range(3):
            sheet.write(i,j,t)
            t+=1
    Excel_book.save('07_test.xlsx')
def get_data():
    data=xlrd.open_workbook('07_test.xlsx')
    # 获取第一个sheet
    sheet=data.sheets()[0]
    # 获取行数和列数
    rows=sheet.nrows # 行
    cols=sheet.ncols # 列
    # 获取行数据
    for i in range(rows):
        print(sheet.row_values(i))
    # 获取列数据
    for j in range(cols):
        print(sheet.col_values(j))
    # 获取指定单元格数据
    print(sheet.cell_value(0,0))
if __name__ == '__main__':
    create()
    get_data()
