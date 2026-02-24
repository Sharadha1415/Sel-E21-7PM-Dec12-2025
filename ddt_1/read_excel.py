import xlrd

def reading_testdata(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)             ## book obj
    worksheet = workbook.sheet_by_name(sheetname)       ## sheet obj
    rows = worksheet.get_rows()                         ## generator obj
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value

    return d






















