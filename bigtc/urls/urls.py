#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base
from handlers import reports
from handlers import crawler

url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/reports", reports.ReportsHandler, None, "reports"),
    ("/test", base.TestHandler, None, "test"),
    ("/crawler", crawler.CrawlerHandler, None, "crawler"),
]
