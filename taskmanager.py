#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random,time,Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


#分布式进程
task_queue=Queue.Queue()
result_queue=Queue.Queue()


class QueueManager(BaseManager):
    pass


def get_task_queue():
    return task_queue

def get_result_queue():
    return result_queue

QueueManager.register('get_task_queue',callable=get_task_queue)
QueueManager.register('get_result_queue',callable=get_result_queue)

manager=QueueManager(address=('127.0.0.1',5000),authkey='abc')


def communicate():
    task=manager.get_task_queue()
    result=manager.get_result_queue()

    for i in range(10):
        n=random.randint(0,10000)
        print "put task %d..."%n
        task.put(n)

    print "try get results..."
    for i in range(10):
        r=result.get(timeout=10)
        print "result: %s" %r


if __name__=="__main__":
    freeze_support()
    manager.start()
    communicate()
    manager.shutdown()
