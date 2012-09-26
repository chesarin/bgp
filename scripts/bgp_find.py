#!/usr/bin/env python
from itertools import islice
import re
response = raw_input("Enter the prefix you are looking for: ")
myfilename = raw_input("Enter the filename to analyze: ")
sentinel = 0
sentinel2 = 0
tmpattern = re.compile (r"(TIME:) (\w+/\w+/\w+ \w+:\w+:\w+)")
tppattern = re.compile (r"(TYPE:) (\w+/\w+)")
vipattern = re.compile (r"(VIEW:) (\w+)")
sepattern = re.compile (r"(SEQUENCE:) (\w+)")
prepattern = re.compile (r"(PREFIX:) (\w+.\w+.\w+.\w+/\w)")
frompattern = re.compile (r"(FROM:) (\w+.\w+.\w+.\w+ \w+)")
origipattern = re.compile (r"(ORIGINATED:) (\w+/\w+/\w+ \w+:\w+:\w+)")
originpattern = re.compile (r"(ORIGIN:) (\w+)")
#aspathpattern = re.compile (r"(ASPATH:) (\w+)")
aspathpattern = re.compile (r"ASPATH: ")
nexthoppattern = re.compile (r"(NEXT_HOP:) (\w+.\w+.\w+.\w+)" )
statspattern = re.compile (r"(STATUS:) (\w+)")
f = open(myfilename,'r')
while True:
    next_12_lines = list(islice(f,12))
    if not next_12_lines:
        break
    else:
        global tm, tp, vip, sep, prep, frompat, origip, originp, aspathp, nexthop, statspat

        for line in next_12_lines:
            if tmpattern.match(line):
                tm = tmpattern.match(line).group(2)
            elif tppattern.match(line):
                tp = tppattern.match(line).group(2)
            elif vipattern.match(line):
                vip = vipattern.match(line).group(2)
            elif sepattern.match(line):
                sep = sepattern.match(line).group(2)
            elif prepattern.match(line):
                prep = prepattern.match(line).group(2)
            elif frompattern.match(line):
                frompat = frompattern.match(line).group(2)
            elif origipattern.match(line):
                origip = origipattern.match(line).group(2)
            elif originpattern.match(line):
                originp = originpattern.match(line).group(2)
            elif aspathpattern.match(line):
                tmp = aspathpattern.split(line)
                #aspathp = aspathpattern.match(line).group(2)
                aspathp = tmp[1]
            elif nexthoppattern.match(line): 
                nexthop = nexthoppattern.match(line).group(2)
            elif statspattern.match(line):
                statspath = statspattern.match(line).group(2)
                
        if ( bool(tm) & bool(tp) & bool(vip) & bool(sep) & bool(prep) & bool(frompat) & bool(origip) & bool(originp) & bool(aspathp) & bool(nexthop) & bool(statspath) ):
            sentinel = sentinel + 1
#            if response == prep:
#            if re.search('\\b'+response+'\\b',aspathp):
            if re.search('\\b'+response+'$',aspathp):
#                print tm, " ", tp, " ", vip, " ", sep, " ", prep, " ", frompat, " ", origip, " ", originp, " ", aspathp, " ", nexthop," ", statspath
                sentinel2 = sentinel2 + 1

f.close()
print "Total number of entries: ", sentinel
print "Total number of match entries: ", sentinel2
