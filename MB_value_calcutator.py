#Conversion factor -> 1024 MB = 1 GB


import re

def get_first_nbr_from_str(input_str):
    '''
    This function was sourced from StackOverflow.
    '''
    if not input_str and not isinstance(input_str, str):
        return 0
    out_number = ''
    for ele in input_str:
        if (ele == '.' and '.' not in out_number) or ele.isdigit():
            out_number += ele
        elif out_number:
            break
    return float(out_number)

# Get filename from user and open the file
FileName = input('Enter the filename(in double quotes) ')
FileName = FileName + ".txt"
f=open(FileName,"r")

#Lists to store numerical values extracted from the strings
arr1 = []
arr2 = []

#Store file data in a list

with open(FileName) as f:
    content = f.readlines()
    content = [x.strip() for x in content]

# Gigabyte values stored in this array
numarray_GB = []

#Megabyte values stored in this array
numarray_MB = []


for i in content:

    i=str(i)
    if(re.search('Gb', i, re.IGNORECASE)):
        arr2.append(i)

    if (re.search('Mb', i, re.IGNORECASE)):
        arr1.append(i)

for i in arr2:
    numarray_GB.append(get_first_nbr_from_str(i))

for i in arr1:
    numarray_MB.append(get_first_nbr_from_str(i))

for i in numarray_MB:
    float(i)
sum1 = 0
sum2 = 0

for i in numarray_MB:
    sum1 = sum1 + i
for i in numarray_GB:
    float(i)
    i = i * 1024
    sum2 = sum2 + i

sum = sum1 + sum2
sum = str(sum)

print("Total memory used is: " + sum + " megabytes.")