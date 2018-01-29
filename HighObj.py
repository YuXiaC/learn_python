#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType

#动态参加成员和函数
"""
class Student(object):
    pass

s=Student()
s.name="Michal"
print s.name

def set_age(self,age):
    self.age=age

s.set_age=MethodType(set_age,s,Student)
s.set_age(25)
print s.age

s2=Student()

#error
#s2.set_age(25)

def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,None,Student)
s.set_score(100)
print s.score

"""



#使用__slots__限制class的属性
"""
class Student(object):
    __slots__=("name",'age')

s=Student()
s.name="Michal"
s.age=25

#error
#s.score=100

#__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的:
class GranduateStudent(Student):
    pass

gs=GranduateStudent()
gs.score=99
print gs.score


#在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class PrimaryStudent(Student):
    __slots__ = ("phone")

ps=PrimaryStudent()
ps.phone="+860000000"
ps.name="Lisa"

#error
#ps.number="1500000"
"""

#使用@property
"""
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=value

    @property
    def age(self):
        return 2018-self._birth

s=Student()
s.score=59
s.birth=1998
#error
#s.age=10
print s.age
"""

#多重继承

