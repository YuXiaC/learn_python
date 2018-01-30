#!/usr/bin/env python
# -*- coding:utf-8 -*-


from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib  #用来抓去网站信息的模块


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        pass
        #print('<%s>' % tag)


    def handle_endtag(self, tag):
        pass
        #print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        pass
        #print('<%s/>' % tag)

    def handle_data(self, data):
        print "data: %s" %data

    def handle_comment(self, data):
        pass
        #print('<!-- -->')

    def handle_entityref(self, name):
        pass
        #print('&%s;' % name)

    def handle_charref(self, name):
        pass
        #print('&#%s;' % name)


#这是一个失败的测试，对于JavaScript乱码
if __name__=="__main__":
    try:
        page = urllib.urlopen('http://so.gushiwen.org/shiwenv_690dc613cb12.aspx')
        # 读取实例内容,赋值给XML
        XML = page.read()
    finally:
        page.close()  # 不能使用with as,貌似实例没有__exit__
    parser = MyHTMLParser()
    parser.feed(XML)