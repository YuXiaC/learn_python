#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())