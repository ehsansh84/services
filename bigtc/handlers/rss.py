#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
# import redis


class RssHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        from pymongo import MongoClient
        con_bigtc = MongoClient()
        db_bigtc = con_bigtc.bigtc
        col_rss = db_bigtc['rss']
        col_rss_log = db_bigtc['rss_log']
        rss = col_rss.find({'active': 1})
        rss_data = []
        for rss_item in rss:
            rounds = 0
            full_rounds = 0
            empty_rounds = 0
            total_new = 0
            rss_log = col_rss_log.find({'link': rss_item['link']})
            for rss_log_item in rss_log:
                rounds += 1
                if rss_log_item['duplicates'] == 0 and rss_log_item['new'] > 0:
                    full_rounds += 1
                if rss_log_item['new'] == 0:
                    empty_rounds += 1
                total_new += rss_log_item['new']
                rss_data.append({
                    'link':rss_log_item['link'],
                    'rounds': rounds,
                    'full_rounds': full_rounds,
                    'empty_rounds': empty_rounds,
                    'total_new': total_new
                })
        self.render('crawler.html', rss_data=rss_data)

