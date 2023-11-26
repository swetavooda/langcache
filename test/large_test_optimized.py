import time
from dataset import read
from langcache.core_optimized import Cache

def test_optimized_largetest():

    cache = Cache(tune_frequency=5, tune_policy="recall")

    for data in read():

        qid1 = data["qid1"]
        qid2 = data["qid2"]
        q1 = data["q1"]
        q2 = data["q2"]
        duplicate = data["duplicate"]

        # Get cache.
        # value = cache.get(q1)
        # if value == None:
        cache.put(q1, str(qid1))
    start_time = time.time()
    cache.extract_features()

    total = 0
    total_similar = 0
    fn, tp, fp =0,0,0

    for data in read():
        total += 1
        qid1 = data["qid1"]
        qid2 = data["qid2"]
        q1 = data["q1"]
        q2 = data["q2"]
        duplicate = data["duplicate"]

        if duplicate:
            total_similar += 1
        # Get cache.
        value = cache.get_features(q2)
        if value == None:
            cache.put(q2, str(qid2))
            if duplicate: fn+=1
        else: 
            if duplicate: tp+=1
            else: fp+=1

    end_time = time.time()

    print("Total pair", total)
    print("Total similar pair", total_similar)
    print("Total time taken after using Precomputed Embeddings for Similarity ", end_time-start_time)

    print("Precision", tp / (tp + fp))
    print("Recall", tp / (tp + fn))
    print("TP FN FP", tp, fn, fp)
