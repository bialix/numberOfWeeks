#!/usr/bin/python

DATE1 = (2013, 01, 07)
DATE2 = (2013, 03, 07)

import datetime

date1 = datetime.date(*DATE1)
date2 = datetime.date(*DATE2)

td = date2 - date1

print "date1: %04d-%02d-%02d" % DATE1
print "date2: %04d-%02d-%02d" % DATE2
print
print "days  passed: %d" % td.days
print "weeks passed: %.1f" % (float(td.days) / 7)
