Confluence Python API
=====================

If you want to interfere with Confluence from Python, this is what you are looking for.

This package is an almost complete rewrite of Sorin Sbarnea's "confluence".
It supports at least Python 2.7 and Python 3.4.

How to use it:

```python
from confluence import Confluence
conf = Confluence("http://localhost:8080", "admin", "admin")
conf.store_page_content("test", "test", "hello world!")
```

Released under Simplified BSD License. Copyright (c) 2015, Samsung Electronics Co.,Ltd.

P.S. Yeah, there are no tests now.