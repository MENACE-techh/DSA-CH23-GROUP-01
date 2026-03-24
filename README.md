# DSA-CH23-GROUP-01
# DSA-CH23-GROUP-01: Scalable URL Shortener (Bitly-Lite)

[cite_start]**Course:** Data Structures and Algorithms [cite: 1]
[cite_start]**Design Methodology:** Chapter 23 System Design (Hemant Jain) [cite: 6]
[cite_start]**Project Variant:** B2 - Custom Aliases + Expiry/TTL Scheduler [cite: 14]

## Team Members
* **Mirriam Moraa (BSCCS/2025/53316)** - Project Lead & Video Production
* **Donson Baragu (BSCCS/2025/53666)** - Core Backend Logic (Hash Maps)
* **Andrew Clyde Otieno (BSCCS/2025/54813)** - System Architect (Scalability)
* **Sheila Wanjigi (BSCCS/2025/52142)** - Quality Assurance & Analytics

---

## [cite_start]1. Use Cases Generation [cite: 7]
* Users can generate a unique short alias for any long URL.
* Users can define custom aliases for branding.
* System automatically expires links after a set Time-To-Live (TTL).
* Users can view and undo recent link creations.

## [cite_start]2. Constraints and Analysis [cite: 7]
* **Latency:** Redirection must occur in near $O(1)$ time to avoid user drop-off.
* **Collision:** Custom aliases must be checked for uniqueness immediately.
* **Throughput:** The system must handle high-volume write and read operations.

## [cite_start]3. Basic Design (DSA Justification) [cite: 7, 8]
* **Hash Table / Map:** The primary storage for URL mapping, ensuring $O(1)$ lookup time for redirections.
* **Stack:** Implemented for a "history" feature, allowing users to backtrack or undo their last five shortened links ($O(1)$ push/pop).
* **Queue:** Powers the TTL Scheduler; expired links are queued for deletion to prevent blocking the main service.
* **Heap / Priority Queue:** Tracks "Top-K" most visited links for the analytics dashboard in $O(\log n)$ time.
* **Sorting & Searching:** Uses Merge Sort ($O(n \log n)$) to organize link history by timestamp and Binary Search ($O(\log n)$) for locating specific user logs.

## [cite_start]4. Bottlenecks [cite: 7]
* **Memory Exhaustion:** As the Hash Map grows, it may exceed RAM capacity.
* **Queue Latency:** If many links expire at once, the cleanup queue may lag.

## [cite_start]5. Scalability [cite: 15]
* **Sharding:** Partitioning the hash table by the first character of the alias to distribute load.
* **Caching:** Using a least-recently-used (LRU) cache for high-traffic URLs.

---

## [cite_start]Complexity Analysis 
* **Redirection:** $O(1)$ (Hash Map lookup).
* **Link Creation:** $O(1)$ average.
* **Undo Action:** $O(1)$ (Stack pop).
* **Analytics Sorting:** $O(n \log n)$.
