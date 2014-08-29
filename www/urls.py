#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Li Lin'

import logging

from transwarp.web import get, view

from apis import api, APIError, APIValueError, APIPermissionError, APIResourceNotFoundError

from models import User, Blog, Comment

@view('blogs.html')
@get('/')
def index():
    blogs = Blog.find_all()
    # 查找登陆用户:
    user = User.find_first('where email=?', 'lnetmor@example.com')
    return dict(blogs=blogs, user=user)

@api
@get('/api/users')
def api_get_users():
    users = User.find_by('order by created_at desc')
    for u in users:
        u.password = '******'
    return dict(users=users)