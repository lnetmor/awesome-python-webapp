#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Li Lin'

from models import User, Blog, Comment

from transwarp import db

db.create_engine(user = 'root', password = '123456', database='awesome')

user = User.find_first('where email = ?', 'lnetmor@gmail.com')

##blog = Blog(user_id = user.id, user_name = user.name, user_image = 'about:blank', 
##	name = u'第一篇博客', summary = u'虽然我们跑通了一个最简单的MVC，但是页面效果肯定不会让人满意。对于复杂的HTML前端页面来说，我们需要一套基础的CSS框架来完成页面布局和基本样式。另外，jQuery作为操作DOM的JavaScript库也必不可少。'
##	content = u"虽然我们跑通了一个最简单的MVC，但是页面效果肯定不会让人满意。对于复杂的HTML前端页面来说，我们需要一套基础的CSS框架来完成页面布局和基本样式。另外，jQuery作为操作DOM的JavaScript库也必不可少。"
##	)

blog2 = Blog(user_id = user.id, user_name = user.name, user_image = 'about:blank', 
	name = "第二篇博客", summary = "虽然我们跑通了一个最简单的MVC，但是页面效果肯定不会让人满意。对于复杂的HTML前端页面来说，我们需要一套基础的CSS框架来完成页面布局和基本样式。另外，jQuery作为操作DOM的JavaScript库也必不可少。",
	content = "虽然我们跑通了一个最简单的MVC，但是页面效果肯定不会让人满意。对于复杂的HTML前端页面来说，我们需要一套基础的CSS框架来完成页面布局和基本样式。另外，jQuery作为操作DOM的JavaScript库也必不可少。"
	)

##blog.insert()
blog2.insert()

#u = User(name='Test', email = 'lnetmor@gmail.com', password = '123456', image='about:blank')

#u.insert()

#print 'new user.id', u.id

#uu = User(name = 'Test2', email = 'test@gmail.com', password = '123', image = '')

#uu.insert()

#print 'new user.id', uu.id

##u1 = User.find_first('where email = ?', 'lnetmor@gmail.com')

##print 'find user\'s name:', u1.name

##u1.delete()

##u2 = User.find_first('where email = ?', 'lnetmor@gmail.com')

##print 'find User:', u2