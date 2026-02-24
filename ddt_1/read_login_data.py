import xlrd

path = r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\ddt\login_credentials.xlsx'


def read_login_credentials():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("Sheet1")
    rows = worksheet.get_rows()
    header = next(rows)

    credentials = []
    for ele in rows:
        credentials.append((ele[0].value, ele[1].value))
    return credentials








