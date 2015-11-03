import os
import string
import csv
##### variables for assignment 
filename = 'CS349-F15 - A2.csv'

with open(filename, 'rb') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if row['TA Marking'] == 'Haiyu']
    ids = [row['Userid'][:8] for row in rows]
    result = ' '.join(ids)
    print result
