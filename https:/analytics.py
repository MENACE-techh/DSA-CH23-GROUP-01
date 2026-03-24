import heapq

class AnalyticsDashboard:
    """
    Demonstrates Heap/Priority Queue usage for Top-K analytics.
    """
    def __init__(self):
        # Min-Heap to track most visited links
        self.click_data = [] 

    def track_click(self, alias, count):
        # O(log n) time to maintain the priority queue 
        heapq.heappush(self.click_data, (count, alias))
        
        # Keep only top 10 (Top-K analysis)
        if len(self.click_data) > 10:
            heapq.heappop(self.click_data)

    def get_trending(self):
        # Returns the highest priority (most visited) links
        return sorted(self.click_data, reverse=True)
