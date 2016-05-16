#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base

url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/reports", base.ReportsHandler, None, "reports"),
]
