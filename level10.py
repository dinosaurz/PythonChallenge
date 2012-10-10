from itertools import groupby, islice


def m_groupby(s):
    for key, group in groupby(s):
        yield str(len(list(group)))
        yield key


def morris():
    morris = '1'
    yield morris
    while True:
        morris = ''.join(m_groupby(morris))
        yield morris

a = list(islice(morris(), 31))

print len(a[30])
