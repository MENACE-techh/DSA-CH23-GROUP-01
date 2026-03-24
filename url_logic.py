import hashlib

class URLShortenerEngine:
    """
    Implements Step 3: Basic Design using Hash Tables for O(1) lookups.
    """
    def __init__(self):
        # Hash Table/Map for core redirection [cite: 19]
        self.url_map = {} 
        # Graph representing referral paths (Short Link -> Target) [cite: 24]
        self.redirection_graph = {} 

    def generate_hash(self, url):
        # Using MD5 hash to simulate a collision-resistant key
        return hashlib.md5(url.encode()).hexdigest()[:6]

    def store_url(self, long_url, custom_alias=None):
        alias = custom_alias if custom_alias else self.generate_hash(long_url)
        
        # O(1) Time Complexity for insertion
        self.url_map[alias] = long_url
        
        # Adding to Graph (Node: Alias -> Node: Long URL) [cite: 24]
        if alias not in self.redirection_graph:
            self.redirection_graph[alias] = []
        self.redirection_graph[alias].append(long_url)
        
        return alias

    def resolve(self, alias):
        # O(1) Time Complexity for lookup [cite: 19]
        return self.url_map.get(alias, "Error: Link not found")
