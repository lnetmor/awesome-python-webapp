#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Li Lin'

'''
A WSGI application entry.
'''

import logging; logging.basicConfig(level=logging.INFO)

import os
import time
from datetime import datetime

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

# init db:
db.create_engine(**configs.db)

# init wsgi app: 
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))

# 定义datetime_filter，输入是t，输出是unicode字符串:
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
# 把filter添加到jinjia2，filter名称为datetime，filter本身是一个函数对象:
template_engine.add_filter('datetime', datetime_filter)

wsgi.template_engine = template_engine

import urls

wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000)