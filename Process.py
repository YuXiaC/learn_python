#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time,random
from multiprocessing import Process,Pool,Queue

#Linux
"""
print 'Process (%s) start...' %os.getpid()
pid=os.fork()
if pid==0:
    print "child process: %s" %os.getpid()
else:
    print "father process %s" %os.getpid()
"""

#windows
def run_proc(name):
    print "Run child process %s (%s)" %(name,os.getpid())

if __name__=="__test__":
    print "parent process %s." %os.getpid()
    p=Process(target=run_proc,args=("test",))
    print "process will start"
    p.start()
    p.join()
    print "process end"


def long_time_task(name):
    print "run task %s (%s)..." %(name,os.getpid())
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print "task %s runs %0.2f seconds" %(name,(end-start))

if __name__=="__test__":
    print "parent process %s" %os.getpid()
    p=Pool()
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print "waiting for all subprocess done..."
    p.close()
    p.join()
    print "all subprocess done."



def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue...' %value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value=q.get(True)
        print 'Get %s from queue.' %value

if __name__=="__test__":
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()


