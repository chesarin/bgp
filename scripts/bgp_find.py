#!/usr/bin/env python
print 'hello'
f = open('rib.20041201.0046.txt','r')
for line in f:
    print line,
f.close()
