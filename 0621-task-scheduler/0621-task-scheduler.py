import heapq
import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Convert the frequency dictionary to a max heap
        freqs = [-freq for _, freq in collections.Counter(tasks).items()]
        heapq.heapify(freqs)
        
        time = 0
        while freqs:
            waitlist = []
            for _ in range(n + 1):
                if freqs:
                    task_freq = heapq.heappop(freqs)
                    if task_freq + 1 < 0:
                        waitlist.append(task_freq + 1)
                time += 1
                if not freqs and not waitlist:
                    break

            for task in waitlist:
                heapq.heappush(freqs, task)

        return time
