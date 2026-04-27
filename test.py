from collections import Counter

def test_distribution(n=100000):
    counts = Counter()

    for _ in range(n):
        cid = weighted_commune_choice()
        counts[cid] += 1

    for cid, count in sorted(counts.items()):
        print(f"{cid}: {round((count/n)*100, 2)}%")