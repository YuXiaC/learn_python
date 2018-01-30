#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


print "a b   c".split(' ')
print re.split(r"\s+","a b   c")

print re.split(r"[\s\,]+","a,b, c  d")

m=re.match(r"^(\d{3})-(\d{3,8})","010-12345hhhh")
print m
print m.group(0)
print m.group(1)
print m.group(2)