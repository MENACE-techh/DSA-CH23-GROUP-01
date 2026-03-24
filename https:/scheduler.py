from collections import deque
import time

class ExpiryScheduler:
    """
    Implements Step 4 & 5: Bottlenecks and Scalability using Queues[cite: 21, 14, 15].
    """
    def __init__(self):
        # Queue for link expiration buffering [cite: 21]
        self.cleanup_queue = deque()

    def schedule_expiry(self, alias, duration=3600):
        expiry_time = time.time() + duration
        self.cleanup_queue.append((alias, expiry_time))

    def run_cleanup(self):
        """
        Simulates scalability: Cleaning up expired items in O(1) time per item.
        Handles the bottleneck of memory exhaustion[cite: 14].
        """
        current_time = time.time()
        removed_count = 0
        while self.cleanup_queue and self.cleanup_queue[0][1] < current_time:
            self.cleanup_queue.popleft() # O(1) operation
            removed_count += 1
        return removed_count
