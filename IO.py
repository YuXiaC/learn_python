#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os
try:
    import cPickle as pickle
    print "import cPickle"
except ImportError:
    import pickle
    print "import pickle"

"""
try:
    f = open('test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
"""

#print sys.getdefaultencoding()#原系统默认编程方式

#print sys.stdout.encoding#现在的编码方式

"""
with open('new.txt', 'r') as f:
    text=f.read()
    #print text
    with open("new2.txt", 'w') as fw:
        fw.write(text)
        fw.close()
    f.close()



with open('new2.txt','r') as f:
    for line in f.readlines():
        print line,
"""

#依旧是乱码
"""
f=open("test.txt",'rb')
u=f.read()
print u
"""

print os.name
#windows 下无uname
#print os.uname()


print os.environ

print os.getenv("PATH")

print os.path.abspath('.')

path=os.path.join("C:\python\learn_python","testdir")
print path
#os.mkdir(path)#绝对路径

#os.rmdir(path)

d=dict(name="Bob",age=20,score=88)
#print pickle.dumps(d)
f=open("dump.txt",'wb')
pickle.dump(d,f)
f.close()

f=open("dump.txt",'rb')
d=pickle.load(f)
f.close()
print d

print json.dumps(d)