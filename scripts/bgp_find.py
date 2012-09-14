#!/usr/bin/env python
import re
response = raw_input("Enter the prefix you are looking for: ")
sentinel = 0
pattern = re.compile ("PREFIX: " + response)
f = open('rib.20041201.0046.txt','r')
for line in f:
    if pattern.match(line):
        sentinel = sentinel + 1
        print line,
f.close()
print ("Total instances of " + response)
print sentinel
