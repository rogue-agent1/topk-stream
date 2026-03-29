#!/usr/bin/env python3
"""Top-K heavy hitters — Space-Saving algorithm."""
import sys

class SpaceSaving:
    def __init__(self, k=10):
        self.k = k
        self.counts = {}
        self.min_count = 0
    def add(self, item):
        if item in self.counts:
            self.counts[item] += 1
        elif len(self.counts) < self.k:
            self.counts[item] = 1
        else:
            min_item = min(self.counts, key=self.counts.get)
            self.min_count = self.counts[min_item]
            del self.counts[min_item]
            self.counts[item] = self.min_count + 1
    def top(self, n=None):
        n = n or self.k
        return sorted(self.counts.items(), key=lambda x: -x[1])[:n]

if __name__ == "__main__":
    import random
    ss = SpaceSaving(10)
    # Zipf-like distribution
    items = []
    for i in range(100):
        freq = max(1, 1000 // (i + 1))
        items.extend([f"item_{i}"] * freq)
    random.shuffle(items)
    for it in items:
        ss.add(it)
    print(f"Processed {len(items)} items, top-10:")
    for item, count in ss.top():
        print(f"  {item}: {count}")
