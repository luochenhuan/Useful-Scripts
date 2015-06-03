import os
import string
import xlrd
import xlwt
from xlutils.copy import copy
##### variables for a*package 
rootdir = 'a1'
markfile = 'a1marks.xls'
markcell = [33,'J']
commentcell = [30,'A']
##### variables for CS349-S15.xlsx 
summaryfile = 'CS349-S15.xlsx'
summarysheet = 'A1'
userID_col = 3
grade_col = 9 
comment_col = 11
linerange = (109,137) # note that the 2nd index is one bigger than end line num
                            # shown in xls file
def col2num(col_ind):
    '''
    ref:
    http://stackoverflow.com/questions/7261936/convert-an-excel-or-spreadsheet-column-letter-to-its-number-in-pythonic-fashion
    '''
    num = 0
    for c in col_ind:
        if c in string.ascii_letters:
            num = num*26 + (ord(c.upper()) - ord('A')) + 1
    return num


def usr_mark_tuple():
    global rootdir
    rootdir = rootdir.rstrip(os.path.sep) #remove the last path slash if there is any
    students = {}
    assert os.path.isdir(rootdir)
    curLevel = rootdir.count(os.path.sep)
    for dir, subdirs, files in os.walk(rootdir):
        if dir.count(os.path.sep) == curLevel+1: #student's assignment folder
            workbook = xlrd.open_workbook(os.path.join(dir,markfile))
            worksheet = workbook.sheet_by_name('Sheet1')
            mark = worksheet.cell_value(markcell[0]-1,markcell[1]-1) 
            comment = worksheet.cell_value(commentcell[0]-1,commentcell[1]-1) 
            students[os.path.basename(dir)] = {'mark': mark, 'comment': comment}
    if dir.count(os.path.sep) > curLevel+1:
        del subdirs[:]
    return students


def copy2xls(students):
    workbook = xlrd.open_workbook(summaryfile)
    worksheet = workbook.sheet_by_name(summarysheet)
    bookcopy = copy(workbook)
    sheetcopy = bookcopy.get_sheet(workbook.sheet_names().index(summarysheet))
    for row in range(linerange[0],linerange[1]):
        usr = worksheet.cell_value(row-1, userID_col-1)        
        sheetcopy.write(row-1, grade_col-1, students[usr]['mark'])
        sheetcopy.write(row-1, comment_col-1, students[usr]['comment'])
    bookcopy.save(summaryfile+'.xls') 


if __name__ == "__main__":
    markcell[1] = col2num(markcell[1]) if type(markcell[1]) is str else markcell[1] 
    commentcell[1] = col2num(commentcell[1]) if type(commentcell[1]) is str else commentcell[1] 
    students = usr_mark_tuple()
    #print students
    copy2xls(students)
