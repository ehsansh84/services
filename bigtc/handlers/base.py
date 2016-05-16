#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('base.html')


class ReportsHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.render('reports.html')

    # def post(self, *args, **kwargs):
    #     print('Hey Shit')
    #     # self.render('reports.html')


