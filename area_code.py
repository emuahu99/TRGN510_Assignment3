#!/usr/bin/python
!head file.txt

with open("file.txt") as file_in:
    for line in file_in:
        print (line[1:4])
