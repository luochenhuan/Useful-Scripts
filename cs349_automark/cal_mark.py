import os
import re
import string
from xlutils.copy import copy

##### variables for assignment 
rootdir = 'a2'
mark_lines = [55, 63, 67, 73, 75, 85, 99, 111, 117, 121, 133, 135, 145, 149, 155]
total_line = 45
comment_line = 165

##### variables for summary excel file
summaryfile = 'CS349-F15.xlsx'
summarysheet = 'A1'
userID_col = 'C'
grade_col = 'G' 
comment_col = 'K'
linerange = (85,104) 

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


def getTotal(userids):
    global rootdir
    marks = {}
    for student in userids:
        filepath = rootdir + '/' + student + '/a2marks.txt'
        total = calTotal(filepath)
        # to do: write to file
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
                print line
                mark = regex.search(line).group(1)
                # print mark
                if len(mark) == 0:
                    print filepath + ' line ' + str(i) + 'has unmarked item'
                else:
                    total += int(mark)

    return total


if __name__ == "__main__":
    students = get_usrid()
    # print '[%s]' % ', '.join(map(str, students))
    print calTotal('a2/apopplew/a2marks.txt')

    # print "Done. Please copy final marks in " + summarysheet +'.xls' + ' to ' + summaryfile
