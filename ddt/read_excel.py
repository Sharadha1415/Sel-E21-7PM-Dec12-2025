import xlrd

path = r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\ddt\reg_data.xlsx'


def read_test_data(sheetname):
    workbook = xlrd.open_workbook(path)             ## Book object
    worksheet = workbook.sheet_by_name(sheetname)       ## Sheet object
    rows = worksheet.get_rows()                     ## generator object
    header = next(rows)
    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value

    return d        ## {'fname': 'Sanchitha', 'lname': 'Ramesh', 'email_id': 'sanchitha@gmail.com', 'pwd': 'sanchitha@12345', 'confirm_pwd': 'sanchitha@12345'}






















































