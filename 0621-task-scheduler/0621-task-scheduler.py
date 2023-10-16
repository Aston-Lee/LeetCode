class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ## maxheap for frequency
        
        # Create a dictionary to count the frequency of each task
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)
        time = 0
        waiting_queue = deque()

        # While there are still tasks or waiting times
        while max_heap or waiting_queue:
            time += 1

            # If there are no more tasks, set time to the next waiting time
            if not max_heap:
                time = waiting_queue[0][1]

            # If there are tasks, take one from the max heap
            else:
                task_count = 1 + heapq.heappop(max_heap)
                if task_count:
                    waiting_queue.append([task_count, time + n])

            # If there are waiting times and the next one has arrived
            if waiting_queue and waiting_queue[0][1] == time:
                heapq.heappush(max_heap, waiting_queue.popleft()[0])
        return time