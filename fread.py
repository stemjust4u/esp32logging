f = open("log.py", "r")
f.read()
f.readline().rstrip("\n")
f.close()

from array import array
import ujson

a = array('f', range(10))
with open('log.py', 'w') as f:
    ujson.dump(tuple(a), f)

with open('log.py', 'r') as f:
    z = array('f', ujson.load(f))

print(z)

dir(uos)
dir(f)
dir(str)
dir(list)
dir(dict)