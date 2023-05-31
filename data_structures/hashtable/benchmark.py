from functools import wraps
from time import time, time_ns

from hash import Hash

def timefunc(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time_ns()
        result = f(*args, **kw)
        te = time_ns()
        print('func:%r with %r items took: %2.4f ns' % \
          (f.__name__, len(args[1]), te-ts))
        return result
    return wrap


def test_insert(ds, keys, values):
    if len(keys) != len(values):
        raise Exception(
            "provide the same number of keys and values. Keys: %r, values: %r",
            len(keys), len(values)
        )

    for i in range(len(keys)):
        ds[keys[i]] =  values[i]

@timefunc
def test_retrieval(ds, keys, values):
    results = []
    for i in range(len(keys)):
        if ds[keys[i]] == values[i]:
            results.append(1)
        else:
            results.append(0)
    return results

@timefunc
def test_search(ds, keys):
    results = []
    for key in keys:
        if key in ds:
            results.append(1)
        else:
            results.append(0)
    return results

if __name__ == '__main__':
    keys = [i for i in range(1000)]
    values = [(10000 - i) for i in range(1000)]

    custom_hash = Hash() 
    test_insert(custom_hash, keys, values)
    insert_result = test_retrieval(custom_hash, keys, values)
    assert all(insert_result)

    py_dict = dict()
    test_insert(py_dict, keys, values)
    insert_result = test_retrieval(py_dict, keys, values)
    assert all(insert_result)
