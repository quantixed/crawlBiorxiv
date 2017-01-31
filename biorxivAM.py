#!/usr/bin/python2.7
from altmetric import Altmetric

a = Altmetric()
try:
    rsp = a.doi("10.1101/095208")
    if rsp is None:
        print "DOI not found"
    else:
        print rsp['score']
except AltmetricHTTPException, e:
    if e.status_code == 403:
        print "You aren't authorized for this call"
    elif e.status_code == 420:
        print "You are being rate limited"
    elif e.status_code == 502:
        print "The API version you are using is currently down for maintenance."
    elif e.status_code == 404:
        print "Invalid API function"
        print e.msg
