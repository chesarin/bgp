#!/usr/bin/env python
from bgp_node import BgpNode
from itertools import islice
from collections import defaultdict
import re
import os
#path = '12242004_txt'
#path = raw_input("Enter the path of files to analyze: ")
tmpattern = re.compile (r"(TIME:) (\w+/\w+/\w+ \w+:\w+:\w+)")
tppattern = re.compile (r"(TYPE:) (\w+/\w+)")
vipattern = re.compile (r"(VIEW:) (\w+)")
sepattern = re.compile (r"(SEQUENCE:) (\w+)")
prepattern = re.compile (r"(PREFIX:) (\w+.\w+.\w+.\w+/\w+)")
frompattern = re.compile (r"(FROM:) (\w+.\w+.\w+.\w+ \w+)")
origipattern = re.compile (r"(ORIGINATED:) (\w+/\w+/\w+ \w+:\w+:\w+)")
originpattern = re.compile (r"(ORIGIN:) (\w+)")
aspathpattern = re.compile (r"ASPATH: ")
nexthoppattern = re.compile (r"(NEXT_HOP:) (\w+.\w+.\w+.\w+)" )
statspattern = re.compile (r"(STATUS:) (\w+)")
def process_file(filename):
    print "processing filename ", filename
    simplelist = []
    mydict = defaultdict(int)
    sentinel = 0
    sentinel2 = 0
    f = open(filename,'r')
    global tm, tp, vip, sep, prep, frompat, origip, originp, aspathp, nexthop, statspat
    mycounter = 0
    for line in f:
        if mycounter == 11:
            sentinel = sentinel + 1
            if re.search('\\b'+response+'$',aspathp):
                asnode = BgpNode(tm,tp,vip,sep,prep,frompat,origip,originp,aspathp,nexthop,statspath)
                simplelist.append(asnode)
                sentinel2 = sentinel2 + 1
            mycounter = 0
        else:
            if tmpattern.match(line):
                tm = tmpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif tppattern.match(line):
                tp = tppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif vipattern.match(line):
                vip = vipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif sepattern.match(line):
                sep = sepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif prepattern.match(line):
                prep = prepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif frompattern.match(line):
                frompat = frompattern.match(line).group(2)
                mycounter = mycounter + 1
            elif origipattern.match(line):
                origip = origipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif originpattern.match(line):
                originp = originpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif aspathpattern.match(line):
                tmp = aspathpattern.split(line)
                aspathp = tmp[1]
                mycounter = mycounter + 1
            elif nexthoppattern.match(line): 
                nexthop = nexthoppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif statspattern.match(line):
                statspath = statspattern.match(line).group(2)
                mycounter = mycounter + 1
    f.close()
    print "Total number of entries: ", sentinel
    print "Total number of match entries: ", sentinel2
    print "Total number of items in list: ", len(simplelist)
    for test in simplelist:
        mydict[test.prefixval] += 1
    #    test.display()

    print "Dictionary has ", len(mydict), " entries in it"
#    keys = mydict.keys()
#    keys.sort()
    outfilename = filename+'prefixes_sorted'
    myoutfile = open(outfilename,'w+')
#    for key in sorted(mydict, key=lambda key: mydict[key]):
    for key in mydict:
#        print key
        entry = key+'\n'
        myoutfile.write(entry)
    myoutfile.close()

def lookasn_prefix_in_file():
    response = raw_input("Enter the AS you are looking for: ")
    myprefix = raw_input("Enter the prefix to look up in file: ")
    filename = raw_input("Enter filename to search in: ")
    print "processing filename ", filename
    simplelist = []
    sentinel = 0
    sentinel2 = 0
    f = open(filename,'r')
    global tm, tp, vip, sep, prep, frompat, origip, originp, aspathp, nexthop, statspat
    mycounter = 0
    for line in f:
        if mycounter == 11:
            sentinel = sentinel + 1
            if re.search('\\b'+response+'$',aspathp) and prep == myprefix:
                asnode = BgpNode(tm,tp,vip,sep,prep,frompat,origip,originp,aspathp,nexthop,statspath)
                simplelist.append(asnode)
                sentinel2 = sentinel2 + 1
            mycounter = 0
        else:
            if tmpattern.match(line):
                tm = tmpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif tppattern.match(line):
                tp = tppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif vipattern.match(line):
                vip = vipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif sepattern.match(line):
                sep = sepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif prepattern.match(line):
                prep = prepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif frompattern.match(line):
                frompat = frompattern.match(line).group(2)
                mycounter = mycounter + 1
            elif origipattern.match(line):
                origip = origipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif originpattern.match(line):
                originp = originpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif aspathpattern.match(line):
                tmp = aspathpattern.split(line)
                aspathp = tmp[1]
                mycounter = mycounter + 1
            elif nexthoppattern.match(line): 
                nexthop = nexthoppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif statspattern.match(line):
                statspath = statspattern.match(line).group(2)
                mycounter = mycounter + 1
    f.close()
    print "Total number of entries: ", sentinel
    print "Total number of match entries: ", sentinel2
    print "Total number of items in list: ", len(simplelist)
    print "Here is the list of items"
    for item in simplelist:
        item.display()

def lookprefix_in_file():
    myprefix = raw_input("Enter the prefix to look up in file: ")
    filename = raw_input("Enter filename to search in: ")
    print "processing filename ", filename
    simplelist = []
    sentinel = 0
    sentinel2 = 0
    f = open(filename,'r')
    global tm, tp, vip, sep, prep, frompat, origip, originp, aspathp, nexthop, statspat
    mycounter = 0
    for line in f:
        if mycounter == 11:
            sentinel = sentinel + 1
            if prep == myprefix:
                asnode = BgpNode(tm,tp,vip,sep,prep,frompat,origip,originp,aspathp,nexthop,statspath)
                simplelist.append(asnode)
                sentinel2 = sentinel2 + 1
            mycounter = 0
        else:
            if tmpattern.match(line):
                tm = tmpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif tppattern.match(line):
                tp = tppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif vipattern.match(line):
                vip = vipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif sepattern.match(line):
                sep = sepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif prepattern.match(line):
                prep = prepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif frompattern.match(line):
                frompat = frompattern.match(line).group(2)
                mycounter = mycounter + 1
            elif origipattern.match(line):
                origip = origipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif originpattern.match(line):
                originp = originpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif aspathpattern.match(line):
                tmp = aspathpattern.split(line)
                aspathp = tmp[1]
                mycounter = mycounter + 1
            elif nexthoppattern.match(line): 
                nexthop = nexthoppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif statspattern.match(line):
                statspath = statspattern.match(line).group(2)
                mycounter = mycounter + 1
    f.close()
    print "Total number of entries: ", sentinel
    print "Total number of match entries: ", sentinel2
    print "Total number of items in list: ", len(simplelist)
    print "Here is the list of items"
    for item in simplelist:
        item.display()

def lookasn_in_file():
    myasn = raw_input("Enter asn to look up in file: ")
    filename = raw_input("Enter filename to search in: ")
    print "processing filename ", filename
    simplelist = []
    mydict = defaultdict(int)
    sentinel = 0
    sentinel2 = 0
    f = open(filename,'r')
    global tm, tp, vip, sep, prep, frompat, origip, originp, aspathp, nexthop, statspat
    mycounter = 0
    for line in f:
        if mycounter == 11:
            sentinel = sentinel + 1
            if re.search('\\b'+myasn+'$',aspathp):
                asnode = BgpNode(tm,tp,vip,sep,prep,frompat,origip,originp,aspathp,nexthop,statspath)
                simplelist.append(asnode)
                sentinel2 = sentinel2 + 1
            mycounter = 0
        else:
            if tmpattern.match(line):
                tm = tmpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif tppattern.match(line):
                tp = tppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif vipattern.match(line):
                vip = vipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif sepattern.match(line):
                sep = sepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif prepattern.match(line):
                prep = prepattern.match(line).group(2)
                mycounter = mycounter + 1
            elif frompattern.match(line):
                frompat = frompattern.match(line).group(2)
                mycounter = mycounter + 1
            elif origipattern.match(line):
                origip = origipattern.match(line).group(2)
                mycounter = mycounter + 1
            elif originpattern.match(line):
                originp = originpattern.match(line).group(2)
                mycounter = mycounter + 1
            elif aspathpattern.match(line):
                tmp = aspathpattern.split(line)
                aspathp = tmp[1]
                mycounter = mycounter + 1
            elif nexthoppattern.match(line): 
                nexthop = nexthoppattern.match(line).group(2)
                mycounter = mycounter + 1
            elif statspattern.match(line):
                statspath = statspattern.match(line).group(2)
                mycounter = mycounter + 1
    f.close()
    print "Total number of entries: ", sentinel
    print "Total number of match entries: ", sentinel2
    print "Total number of items in list: ", len(simplelist)
#    print "Here is the list of items"
#    for item in simplelist:
#        item.display()
    for test in simplelist:
        mydict[test.prefixval] += 1
    print "Dictionary has ", len(mydict), " entries in it"
    outfilename = filename+'prefixes_sorted'
    myoutfile = open(outfilename,'w+')
    for key in mydict:
#        print key
        entry = key+'\n'
        myoutfile.write(entry)
    myoutfile.close()



def all_files():
    response = raw_input("Enter the AS you are looking for: ")
    path = raw_input("Enter the path of files to analyze: ")
    listing = os.listdir(path)
    for infile in sorted(listing):
        #print "current file is: ", infile
        myfile = path+'/'+infile
        process_file(myfile)

#Start calling functions here
#lookasn_in_file()
#lookprefix_in_file()
#lookasn_in_file()
lookasn_prefix_in_file()
