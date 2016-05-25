#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import redis


class CrawlerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        r_server = redis.Redis('localhost')
        crawler_data = {
            'status': '',
            'expire': -1
        }
        action = self.get_argument('action', '')
        if action == 'start':
            r_server.set('crawler_stat', 'Running')
            r_server.expire('crawler_stat', 20)
            crawler_data['status'] = 'Running'
            crawler_data['expire'] = 20
        elif action == 'update':
            crawler_data['status'] = r_server.get('crawler_stat')
            crawler_data['expire'] = r_server.ttl('crawler_stat')

            # self.write('Started')
        self.render('crawler.html', crawler_data=crawler_data)

