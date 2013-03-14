alfred-python
=============

simple Python access to the Alfred workflow API. If you need inspiration of how to use it, look at the following lines:

```python
import alfred

print alfred.preferences['bundleid'] == alfred.bundleid # access to info.plist
cache = alfred.path(volatile=True) # access to (and creation of) the recommended storage paths

(parameter, query) = alfred.args() # proper decoding and unescaping of command line arguments
results = [alfred.result(
    uid=0,
    arg='https://github.com/nikipore/alfred-python',
    title=parameter,
    subtitle='simple access to the Alfred workflow API',
    icon='icon.png'
)] # a class for each Alfred result
xml = alfred.xml(results) # compiles the XML answer
alfred.write(xml) # writes the XML back to Alfred
```