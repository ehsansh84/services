#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('base.html')


class ReportsHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # action = self.get_argument('action', '')
        self.render('reports.html')

    def post(self, *args, **kwargs):
        from pymongo import MongoClient
        con_bigtc = MongoClient()
        # db_bigtc = con_bigtc.services
        db_bigtc = con_bigtc.bigtc
        col_news = db_bigtc['news']
        col_rss = db_bigtc['rss']
        col_sources = db_bigtc['sources']
        col_categories = db_bigtc['categories']
        news_count = col_news.find().count()
        rss_count = col_rss.find().count()
        rss_active = col_rss.find({'active': 1}).count()
        rss_inactive = rss_count - rss_active

        # This is only an example
        # db.domain.update({},{$unset: {affLink:1}},{multi: true});


        # # Create source collection from RSS collection
        # col_sources.drop()
        # rss = col_rss.find()
        # for item in rss:
        #     if col_sources.find({'name': item['source']}).count() == 0:
        #         col_sources.insert({'name': item['source']})





        # # Updating source table
        # sources = col_sources.find()
        # for item in sources:
        #     news_source = col_news.find({'source': item['name']}).count()
        #     col_sources.update({'name': item['name']}, {'$set': {
        #         'total_news': news_source
        #     }})


        # Generates all categories from news
        news = col_news.find()
        i = 1
        for item in news:
            if i % 10000 == 0:
                self.write(i)
                # print(i)
            i += 1
            if col_categories.find({'name': item['category']}).count() == 0:
                col_categories.insert({
                    'name': item['category'],
                    'count': 0
                })



        # Updates categories news count
        categories = col_categories.find()
        i = 1
        for item in categories:
            print(i)
            i += 1
            count = col_news.find({'category': item['name']}).count()
            col_categories.update({'name': item['name']}, {'$set': {'count': count}})





        self.write('Documents summary:<br> %s <br>' % (30 * '='))
        self.write('Total documents: %s<br>' % news_count)
        self.write('Total RSS: %s<br>' % rss_count)
        self.write('Total RSS active: %s<br>' % rss_active)
        self.write('Total RSS inactive: %s<br>' % rss_inactive)


        # Print sources
        sources = col_sources.find().sort('total_news', -1).limit(10)
        self.write('<br>These are top 10 of news sources:<br>')
        self.write(30 * '=')
        self.write('<br>')
        for item in sources:
            self.write('Source: %s News count: %s<br>' % (item['name'], item['total_news']))


        # Print Categories
        categories = col_categories.find().sort('count',-1).limit(10)
        self.write('<br>These are top 10 of news categories:<br>')
        self.write(30 * '=')
        self.write('<br>')
        for item in categories:
            self.write('Category: %s News count: %s<br>' % (item['name'], item['count']))



        # name = self.get_argument('name', 'ok')
        # self.write('Hey Shit')
        # print(news_count)
        # self.write('Name:')
        # self.write(name)
        # self.render('reports.html')


