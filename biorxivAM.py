#!/usr/bin/python2.7
from altmetric import Altmetric

def getAMFromDOI(link):
    try:
        rsp = a.doi(link)
        if rsp is None:
            print "DOI not found"
        else:
            out = rsp['score']
    except AltmetricHTTPException, e:
#        if e.status_code == 403:
#            print "You aren't authorized for this call"
#        elif e.status_code == 420:
#            print "You are being rate limited"
#        elif e.status_code == 502:
#            print "The API version you are using is currently down for maintenance."
#        elif e.status_code == 404:
#            print "Invalid API function"
            out = e.msg
    return out

a = Altmetric()
with open("todoDOIs.txt", "rb") as infile:
    myDOIs = [line[:-1] for line in infile]
with open("doi2AM.txt", "a") as outfile:
    for curDOI in myDOIs:
        am = getAMFromDOI(curDOI)
        print >> outfile, curDOI + '\t' + am
