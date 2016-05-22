#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web


class ReportsHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # action = self.get_argument('action', '')

        from pymongo import MongoClient
        con_bigtc = MongoClient()
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


        # # Generates all categories from news
        # news = col_news.find()
        # i = 1
        # for item in news:
        #     if i % 10000 == 0:
        #         self.write(str(i))
        #         # print(i)
        #     i += 1
        #     if col_categories.find({'name': item['category']}).count() == 0:
        #         col_categories.insert({
        #             'name': item['category'],
        #             'count': 0
        #         })



        # # Updates categories news count
        # categories = col_categories.find()
        # i = 1
        # for item in categories:
        #     print(i)
        #     i += 1
        #     count = col_news.find({'category': item['name']}).count()
        #     col_categories.update({'name': item['name']}, {'$set': {'count': count}})




        summary_items = [
            {'name': 'Documents count', 'value': news_count},
            {'name': 'RSS count', 'value': rss_count},
            {'name': 'RSS active count', 'value': rss_active},
            {'name': 'RSS inctive count', 'value': rss_inactive},
            {'name': 'Documents count', 'value': news_count},
        ]

        # Print sources
        sources_items = [
        ]
        sources = col_sources.find().sort('total_news', -1).limit(10)
        # self.write('<br>These are top 10 of news sources:<br>')
        # self.write(30 * '=')
        # self.write('<br>')
        for item in sources:
            sources_items.append({'name': item['name'], 'value': item['total_news']})

            # self.write(': %s News count: %s<br>' % (item['name'], item['total_news']))


        # Print Categories
        categories_items = []
        categories = col_categories.find().sort('count',-1).limit(10)
        # self.write('<br>These are top 10 of news categories:<br>')
        # self.write(30 * '=')
        # self.write('<br>')
        for item in categories:
            categories_items.append({'name': item['name'], 'value': item['count']})

            # self.write('Category: %s News count: %s<br>' % (item['name'], item['count']))



        # name = self.get_argument('name', 'ok')
        # self.write('Hey Shit')
        # print(news_count)
        # self.write('Name:')
        # self.write(name)
        # self.render('reports.html')


        self.render('reports.html',
                    summary_items=summary_items,
                    sources_items=sources_items,
                    categories_items=categories_items
                    )

