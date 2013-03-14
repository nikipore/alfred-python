alfred-python
=============

simple Python access to the Alfred workflow API. If you need inspiration of how to use it, look at the following lines:

```python
(parameter, query) = alfred.args() # proper decoding and unescaping of command line arguments
results = [alfred.result(
    uid=0,
    arg='https://github.com/nikipore/alfred-python',
    title=parameter,
    subtitle='simple access to the Alfred workflow API',
    icon='icon.png'
)]
xml = alfred.xml(results) # compiles the XML result
alfred.write(xml) # writes the XML back to Alfred
```