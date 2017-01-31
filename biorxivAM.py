#!/usr/bin/python2.7
from altmetric import Altmetric

def getAMFromDOI(link):
    rsp = a.doi(link)
    out = "a"
    if rsp is None:
        print "DOI not found"
    else:
        out = str(rsp['score'])
    return out

a = Altmetric()
with open("todoDOIs.txt", "rb") as infile:
    myDOIs = [line[:-1] for line in infile]
with open("doi2AM.txt", "a") as outfile:
    for curDOI in myDOIs:
        am = getAMFromDOI(curDOI)
        print >> outfile, curDOI + '\t' + am
