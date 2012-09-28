#!/usr/bin/env python
class BgpNode:
    def __init__(self,timeval,typeval,viewval,sequenceval,prefixval,fromval,originatedval,originval,aspathval,next_hopval,statusval):
        self.timeval = timeval
        self.typeval = typeval
        self.viewval = viewval
        self.sequenval = sequenceval
        self.prefixval = prefixval
        self.fromval = fromval
        self.originatedval = originatedval
        self.originval = originval
        self.aspathval = aspathval
        self.next_hopval = next_hopval
        self.statusval = statusval
    def display(self):
        print self.timeval," ",self.originatedval," ",self.prefixval," ",self.fromval," ",self.aspathval.rstrip('\n')

    def get_prefix(self):
        print self.prefixval
