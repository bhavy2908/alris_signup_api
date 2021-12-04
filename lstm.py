import xlrd


def alris_lstm(amount, des_return, time_period, khatka):
    loc = ('xl.xls')

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    factor = []
    invest_to = []
    counter = 0
    arr = []
    for i in range(sheet.nrows):
        factor.append(int(sheet.cell_value(i, 2)))
        invest_to.append(sheet.cell_value(i, 1))
    high = ["BRDS", "SNOW", "AUPH", "LFST", "CLVT"]
    med = ["ES=F", "YM=F", "NQ=F", "RTY=F", "ZB=F"]
    low = ["UMPIX", "UMPSX", "ENPSX", "ENPIX", "FSDAX"]
    if khatka == "Low":
        counter = 0
        arr = low
    elif khatka == "Medium":
        counter = 5
        arr = med
    elif khatka == "High":
        counter = 10
        arr = high
    mon_ret = des_return / time_period / 12

    mon_investment1 = mon_ret * 100 / (1 + factor[counter])
    mon_investment2 = mon_ret * 100 / (1 + factor[counter + 1])
    mon_investment3 = mon_ret * 100 / (1 + factor[counter + 2])
    mon_investment4 = mon_ret * 100 / (1 + factor[counter + 3])
    mon_investment5 = mon_ret * 100 / (1 + factor[counter + 4])

    invest1 = invest_to[counter]
    invest2 = invest_to[counter + 1]
    invest3 = invest_to[counter+2]
    invest4 = invest_to[counter+3]
    invest5 = invest_to[counter+4]

    return [[mon_investment1, mon_investment2, mon_investment3, mon_investment4, mon_investment5],[invest1, invest2, invest3, invest4, invest5]]
