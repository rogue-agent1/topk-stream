#!/usr/bin/env python3
"""topk_stream - Streaming top-K elements with min-heap."""
import sys, heapq, random, time, json

def topk_stream(iterable, k=10, key=None):
    heap = []
    for item in iterable:
        val = key(item) if key else item
        if len(heap) < k:
            heapq.heappush(heap, (val, item))
        elif val > heap[0][0]:
            heapq.heapreplace(heap, (val, item))
    return sorted(heap, reverse=True)

def demo():
    random.seed(42)
    data = [random.randint(1, 10000) for _ in range(100000)]
    k = 10
    start = time.time()
    result = topk_stream(data, k)
    elapsed = time.time() - start
    print(f"Top {k} from {len(data):,} elements ({elapsed*1000:.1f}ms):")
    for score, item in result:
        print(f"  {item:>6}")
    # Verify
    actual = sorted(data, reverse=True)[:k]
    print(f"\n  Correct: {[item for _,item in result] == actual}")

def from_stdin(k=10):
    values = []
    for line in sys.stdin:
        for tok in line.split():
            try: values.append(float(tok))
            except: pass
    result = topk_stream(values, k)
    for score, item in result:
        print(f"  {item}")

def main():
    args = sys.argv[1:]
    if not args or args[0] == 'demo': demo()
    elif args[0] == '-h': print("Usage: topk_stream.py demo | topk_stream.py K < data")
    else:
        k = int(args[0]) if args[0].isdigit() else 10
        from_stdin(k)

if __name__ == '__main__': main()
