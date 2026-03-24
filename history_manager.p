import time

class UserHistory:
    """
    Handles Stack-based undo/history and Sorting/Searching.
    """
    def __init__(self):
        # Stack for backtracking/undo (LIFO) [cite: 20]
        self.history_stack = []
        self.all_logs = []

    def push_to_history(self, alias):
        # O(1) push operation
        self.history_stack.append((alias, time.time()))
        self.all_logs.append({"alias": alias, "time": time.time()})

    def undo_last_creation(self):
        # O(1) pop operation for undo functionality [cite: 20]
        if not self.history_stack:
            return None
        return self.history_stack.pop()

    def get_sorted_logs(self):
        # Implementing O(n log n) Merge Sort for logs [cite: 25]
        # In Python, sorted() uses Timsort which is O(n log n)
        return sorted(self.all_logs, key=lambda x: x['time'], reverse=True)
