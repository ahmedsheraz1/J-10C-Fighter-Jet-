Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import json
json.loads('["foo", {"bar":["J-10C", null, 1.8, 2]}]')
['foo', {'bar': ['J-10C', None, 1.8, 2]}]
json.loads('"\\"foo\\bar"')
'"foo\x08ar'
from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)
['streaming API']
