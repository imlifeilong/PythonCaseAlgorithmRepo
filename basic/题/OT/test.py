import heapq
from collections import defaultdict


class SlidingWindowMinHeap:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def push(self, url, count):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, (count, url))
        else:
            if count > self.heap[0][0]:
                # heapq.heappop(self.heap)
                heapq.heapreplace(self.heap, (count, url))

    def get_top_k(self):
        top_k = [(count, url) for count, url in self.heap]
        top_k.sort(reverse=True)
        return top_k


def process_streaming_data(log_file, k):
    url_counts = defaultdict(int)
    min_heap = SlidingWindowMinHeap(k)

    with open(log_file, 'r') as f:
        for line in f:
            url = line.strip()
            url_counts[url] += 1
            min_heap.push(url, url_counts[url])

    return min_heap.get_top_k()


# Example usage:
log_file = 'access.log'
k = 10
result = process_streaming_data(log_file, k)

print(f"Top {k} URLs:")
for count, url in result:
    print(f"{url}: {count}")
