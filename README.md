alfred-python
=============

simple Python access to the Alfred workflow API. If you need inspiration of how to use it, look at the following lines:

```python
import alfred

>>> import alfred
>>> print alfred.bundleid
nikipore.alfredpython
>>> print alfred.preferences['description']
Python library for Alfred workflow API
>>> alfred.bundleid
'nikipore.alfredpython'
>>> alfred.preferences['description'] # access to info.plist
'Python library for Alfred workflow API'
>>> alfred.work(volatile=True) # access to (and creation of) the recommended storage paths
'/Users/jan/Library/Caches/com.runningwithcrayons.Alfred-2/Workflow Data/nikipore.alfredpython'
>>> alfred.work(volatile=False)
'/Users/jan/Library/Application Support/Alfred 2/Workflow Data/nikipore.alfredpython'
>>> alfred.config()
'config'
```

The boilerplate for your Alfred workflow is reduced to something like this:

```python
# -*- coding: utf-8 -*-
(parameter, query) = alfred.args() # proper decoding and unescaping of command line arguments
results = [alfred.result(
    uid=0,
    arg=u'https://www.google.de/q=%s' % query,
    title=parameter,
    subtitle=u'simple access to the Alfred workflow API',
    icon='icon.png'
)] # a single Alfred result
xml = alfred.xml(results) # compiles the XML answer
alfred.write(xml) # writes the XML back to Alfred
```