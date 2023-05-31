# Hash Table
Also known as Dictionary, Associative Array, HashMap etc.

## Runtime 
Python 3.10

## Details
We implemented this hash table using a list. A hash index is
generated with a modulo operator. We implemented separate
chaining mechanism to address hash collision. The actual key
value pairs are stored in a linked list. The hash function
generates an index which we use to get to the desired slot
in the first level list that holds the heads of the linked
list

## Limitations
At this moment, the hashtable can only work with numeric keys.
So string, sets etc cannot be used as keys.

## How to Use 
You can use this how you would use a regular python dictionary with
one exception. When initializing a new hash, you have to declare it
like a python object, `Hash()`.

```
>>> from hash import Hash
>>> h = Hash()

>>> h[10] = 10
>>> h[10]
10
>>> 10 in h
True
>>> 100 in h
False
>>> h[110] = 110
>>> h[110]
110

```
## Benchmark
Since this is a rather naive implementation, it is quite slower than
CPython's dictionary implementation.

For example, to retrive 1000 items fron this data structure,
Hash takes: 1574309 ns, while python's dictionary takes 195097 ns.
Hash is about 8x slower in this case. Generally speaking, I have noticed
one order of magnitude difference between the two.

Feel free to look at the code in `benchmark.py` for more details.
