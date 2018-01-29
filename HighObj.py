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
"""
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
"""

#定制类
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "Student object (name:%s)"%self.name

    #为调试服务
    __repr__=__str__

print Student("Michal")


class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

for n in Fib():
    print n,
print

print Fib()[5]

f=Fib()

print f[:10]


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

print Chain().status.user.timeline.list
print Chain().users('michael').repos



"""
要创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

"""
def fn(self,name="world"):
    print ("hello, %s"%name)

Hello=type("Hello",(object,),dict(hello=fn))


#MetaClass
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)


class MyList(list):
    __metaclass__ = ListMetaclass

L=MyList()
L.add(1)
L.add(2)
print L


#Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


#详细类型
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()