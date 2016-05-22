#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base
from handlers import reports

url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/reports", reports.ReportsHandler, None, "reports"),
    ("/test", base.TestHandler, None, "test"),
]
