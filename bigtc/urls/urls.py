#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base
from handlers import reports
from handlers import crawler
from handlers import rss

url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/reports", reports.ReportsHandler, None, "reports"),
    ("/test", base.TestHandler, None, "test"),
    ("/crawler", crawler.CrawlerHandler, None, "crawler"),
    ("/rss", rss.RssHandler, None, "rss"),
]