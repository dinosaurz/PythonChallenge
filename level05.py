import pickle

pickled = "./extras/banner.p"

handle = pickle.load(open(pickled))
for line in handle:
    print ''.join(map(lambda pair: pair[0] * pair[1], line))
