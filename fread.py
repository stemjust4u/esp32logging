'''
3 methods to read/write a file
    1         2          3
f.write() ujson.dump pickle.dump
f.read()  ujson.load pickle.load

'''

f = open("log.py", "r")
f.read()
f.readline().rstrip("\n")
f.close()

from array import array
import ujson

a = array('f', range(10))
a = {"key1":1, "key2":2}
f = open('test.csv', 'w')
with open('log.py', 'w') as f:
    ujson.dump(tuple(a), f)

ujson.dump(a, f)

f = open('test.csv', 'r')
with open('log.py', 'r') as f:
    z = array('f', ujson.load(f))

z = ujson.load(f)
print(z)
''' To use pickle just search/replace ujson with pickle

JSON supports a more limited range of Python data types whereas pickle 
supports all native data types. JSON has the benefit of being a standard, 
so JSON files may easily be accessed by other languages. Note that arrays 
are not a native data type so need to be converted to tuples when using either 
module as in the sample above.
'''
dir(uos)
dir(f)
dir(str)
dir(list)
dir(dict)