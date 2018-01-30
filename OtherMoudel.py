#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from collections import defaultdict
from collections import OrderedDict
import itertools

Point=namedtuple("Point",['x','y'])
p=Point(1,2)
print p.x,p.y
print type(p)


dd=defaultdict(lambda :'N/A')
dd['key1']='abds'
print dd["key1"],dd["key2"]

d=dict([('a',1),('b',2),('c',3)])
print d

#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od=OrderedDict([('a',1),('b',2),('c',3)])
print od


ns=itertools.repeat('ABC',10)
for n in ns:
    print n


for c in itertools.chain('ABC', 'XYZ'):
    print c


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)