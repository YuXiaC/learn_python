#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib  #用来抓去网站信息的模块
from xml.parsers.expat import ParserCreate  #解析器
import re  #正则表达式

try:
    #创建链接实例,获取百度天气API
    page = urllib.urlopen('http://api.map.baidu.com/telematics/v2/weather?location=%E4%BD%9B%E5%B1%B1&ak=B8aced94da0b345579f481a1294c9094')
    #读取实例内容,赋值给XML
    XML = page.read()
finally:
    page.close() #不能使用with as,貌似实例没有__exit__

a = re.compile(r'^\s+$')  #空格,正则表达式

class BaiduWeatherSaxHandler(object):
    def __init__(self):
        self.L = []  #创建一个list装XML中的关键数据
        self.R = False   #当start_element获得的name与
        self.d = ['currentCity','date','weather','wind','temperature']
    def start_element(self,name,attrs):
        # print ('sax:start_element:%s,attrs:%s' % (name,str(attrs)))
        if name in self.d:
            self.R = True
    def end_element(self, name):
        # print ('sax:end_element: %s' % name)
        if name == 'result':  #只让程序显示当天的天气(API中还有未来几天的)
            for x in self.L:
                print x
            raise SystemExit  #关闭程序

    def char_data(self, text):

        if a.match(text):  #去掉空格的(没内容的)
            pass
        elif self.R:
            self.L.append(text)
            self.R = False
        # else:
        #     print ('sax:char_data: %s' % text)

handler =BaiduWeatherSaxHandler()  #设置解析方法
parser =ParserCreate()  #创建解析器
# 设置解析器参数
parser.returns_unicode = True  #返回unicode编码
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(XML)  #解析文本