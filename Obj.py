#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
print bart.get_grade()

#和静态语言不同，Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
bart.age=8
print bart.age


class Animal(object):
    def run(self):
        print 'Animal is running...'

#继承
class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

#多态
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

a=Animal()
print type(a)

print type('abd')==types.StringType

print dir('abc')

#如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法
class MyObject(object):
    def __int__(self):
        self.x=9
    #def __len__(self):
    #    return 100

    def power(self):
        return self.x*self.x

obj=MyObject()
#print len(obj)

#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
print hasattr(obj,'x') #此处应该有问题
setattr(obj,'y',19)
print hasattr(obj,'y')
print obj.y
print hasattr(obj,'power')