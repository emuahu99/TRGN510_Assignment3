#!/usr/bin/python
import sys
import fileinput
import re
import json
my_dict_file= sys.argv[1]
output=[]
i=0
for line in fileinput.input(my_dict_file):
    i=i+1
    splitcolumn_array = re.split('\t',line)
    if "gene" in splitcolumn_array:
        a = re.split(';',splitcolumn_array[8])
        b=re.split(" ",a[1])
        thisdict ={
        "geneName": b[2].strip("\""),
        "chr": splitcolumn_array[0],
        "startPos": int(splitcolumn_array[3]),
        "endPos":int(splitcolumn_array[4])}
        en = json.dumps(thisdict) 
        #en= '{%s}' % ', '.join(['"%s": "%s"' % (k, v) for k, v in thisdict.items()])
        output.append(en) 
print('[\n%s\n]' % ',\n'.join(map(str, output)))
