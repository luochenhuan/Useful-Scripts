import os
import re
import string
import xlrd
from xlutils.copy import copy

from tempfile import mkstemp
from shutil import move

##### variables for assignment 
rootdir = 'a2'
mark_lines = [55, 63, 67, 73, 75, 85, 99, 111, 117, 121, 133, 135, 145, 149, 155]
total_line = 45
comment_line = 165

##### variables for summary excel file
summaryfile = 'CS349-F15.xlsx'
summarysheet = 'A2'
userID_col = 'B'
grade_col = 'G' 
comment_col = 'H'
linerange = (2,21) 

def get_usrid():
    global rootdir
    rootdir = rootdir.rstrip(os.path.sep) #remove the last path slash if there is any
    students = []
    assert os.path.isdir(rootdir)
    curLevel = rootdir.count(os.path.sep)
    for dir, subdirs, files in os.walk(rootdir):
        if dir.count(os.path.sep) == curLevel+1: #student's assignment folder
            students.append(os.path.basename(dir))
    return students

# http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
def getTotal(userids):
    global rootdir
    marks = {}
    for student in userids:
        filepath = rootdir + '/' + student + '/a2marks.txt'
        newpath = rootdir + '/' + student + '/a2_marks.txt'
        total = calTotal(filepath)
        print student + ': ' + str(total)
        marks[student] = total
        # to do: write to file
        with open(newpath,'w') as nf:
            with open(filepath) as old_file:
                i = 0
                for line in old_file:
                    i+=1
                    if i == total_line:
                        line = str(total) + line
                    nf.write(line)

    return marks
        

def calTotal(filepath):
    total = 0
    regex = re.compile("\((.*?)/")
    with open(filepath) as f:
        lines = f.read().splitlines()
        i = 0
        for line in lines:
            i+=1
            if i in mark_lines:
                # print line
                mark = regex.search(line).group(1)
                # print mark
                if len(mark) == 0:
                    print filepath + ' line ' + str(i) + 'has unmarked item'
                else:
                    total += int(mark)

    return total
                

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


def copy2xls(students):
    workbook = xlrd.open_workbook(summaryfile)
    worksheet = workbook.sheet_by_name(summarysheet)
    bookcopy = copy(workbook)
    sheetcopy = bookcopy.get_sheet(workbook.sheet_names().index(summarysheet))
    for row in range(linerange[0],linerange[1]+1):
        usr = worksheet.cell_value(row-1, col2num(userID_col)-1)
        usr = usr[:8] if len(usr) > 8 else usr      
        sheetcopy.write(row-1, col2num(grade_col)-1, students[usr])
    bookcopy.save(summarysheet +'.xls')


if __name__ == "__main__":
    students = get_usrid()
    # print '[%s]' % ', '.join(map(str, students))
    marks = getTotal(students)
    copy2xls(marks)
    print "Done. Please copy final marks in " + summarysheet +'.xls' + ' to ' + summaryfile
