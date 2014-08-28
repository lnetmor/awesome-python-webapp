#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Li Lin'

from models import User, Blog, Comment

from transwarp import db

db.create_engine(user = 'root', password = '123456', database='awesome')

u = User(name='Test', email = 'lnetmor@gmail.com', password = '123456', image='about:blank')

u.insert()

print 'new user.id', u.id

u1 = User.find_first('where email = ?', 'lnetmor@gmail.com')

print 'find user\'s name:', u1.name

u1.delete()

u2 = User.find_first('where email = ?', 'lnetmor@gmail.com')

print 'find User:', u2