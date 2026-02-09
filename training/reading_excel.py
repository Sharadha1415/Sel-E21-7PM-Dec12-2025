'''
xlrd    :   To read excel files, we use xlrd

            To install xlrd
            Go to command prompt    --> pip install xlrd==1.2.0

            STEP1   :   import xlrd
            STEP2   :   open the excel file
                        workbook = xlrd.open_workbook("path_of_excel_file")
            STEP3   :   open the worksheet
                        worksheet = workbook.sheet_by_name("SheetName")

'''

import xlrd

path = r'/files_/student_data.xlsx'

## open the excel file
workbook = xlrd.open_workbook(path)
# print(workbook)         ## Book object

## open the worksheet
worksheet = workbook.sheet_by_name("Sheet1")
# print(worksheet)        ## Sheet object

## convert the sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)             ## generator object

##--------------------------------------------------------------------------

res = next(rows)
# for ele in rows:
#     print(ele)
#
# ## [text:'student_name', text:'age', text:'course', text:'city']
# ## [text:'Sanchitha', number:20.0, text:'BE', text:'Bengaluru']
# ## [text:'Vijayalakshmi', number:22.0, text:'Btech', text:'Mysuru']
# ## [text:'Chandana', number:24.0, text:'Mtech', text:'Hubli']
# ## [text:'Pooja', number:26.0, text:'BE', text:'Gulbarga']

##--------------------------------------------------------------------------

# for ele in rows:
#     print(ele[0], ele[1], ele[2], ele[3])
#
# ## text:'student_name' text:'age' text:'course' text:'city'
# ## text:'Sanchitha' number:20.0 text:'BE' text:'Bengaluru'
# ## text:'Vijayalakshmi' number:22.0 text:'Btech' text:'Mysuru'
# ## text:'Chandana' number:24.0 text:'Mtech' text:'Hubli'
# ## text:'Pooja' number:26.0 text:'BE' text:'Gulbarga'

##--------------------------------------------------------------------------

# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value, ele[3].value)
#
# ## student_name age course city
# ## Sanchitha 20.0 BE Bengaluru
# ## Vijayalakshmi 22.0 Btech Mysuru
# ## Chandana 24.0 Mtech Hubli
# ## Pooja 26.0 BE Gulbarga

##--------------------------------------------------------------------------

# ## using next()
# print(next(rows))       ## [text:'student_name', text:'age', text:'course', text:'city']
# print(next(rows))       ## [text:'Sanchitha', number:20.0, text:'BE', text:'Bengaluru']
# print(next(rows))       ## [text:'Vijayalakshmi', number:22.0, text:'Btech', text:'Mysuru']

##--------------------------------------------------------------------------

# for ele in rows:
#     print(ele[0].value)

##--------------------------------------------------------------------------

# i = 0
# for ele in rows:
#     i += 1
#     if i==3:
#         print(ele)
#         break
























