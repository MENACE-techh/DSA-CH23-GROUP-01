# DSA-CH23-GROUP-01: Scalable URL Shortener System (Bitly-Lite)
**Unit:** Data Structures and Algorithms  
**Design Methodology:** Chapter 23 System Design (Hemant Jain)
**Project Variant:** B2 - Custom Aliases + Expiry/TTL Scheduler

---

## Team Members & Roles
* **Mirriam Moraa (BSCCS/2025/53316)** - **Group Leader:** System Integration & Analytics (Heap)
* **Donson Baragu (BSCCS/2025/53666)** - **Lead Backend:** Core Hashing Engine (Hash Maps & Graphs)
* **Andrew Clyde Otieno (BSCCS/2025/54813)** - **System Architect:** Scalability & TTL Scheduling (Queues)
* **Sheila Wanjigi (BSCCS/2025/52142)** - **Quality Assurance:** History & Undo Logic (Stacks & Sorting)

---

## 1. Use Cases Generation
Our system focuses on providing a reliable, high-speed URL redirection service with the following capabilities:
* **Shortening:** Converting long URLs into unique 6-character short aliases.
* **Customization:** Allowing users to define their own easy-to-remember aliases.
* **Expiration (TTL):** Automatically cleaning up links after a set period to save memory.
* **History/Undo:** Tracking a user's recent actions and allowing them to revert the last link creation.
* **Analytics:** Real-time tracking of the most visited (Top-K) links.

## 2. Constraints and Analysis
* **Latency:** Redirection must be $O(1)$ to ensure a seamless user experience.
* **Storage:** With millions of URLs, the system must utilize memory-efficient data structures.
* **Integrity:** Custom aliases must be checked for collisions before being stored.
* **Availability:** The expiry scheduler must run in the background without locking the main database.

## 3. Basic Design (DSA Justification)
Following the requirements of the course, we have implemented and justified the following structures:



* **Hash Table / Map:** (In `url_logic.py`) The backbone of the system. Provides $O(1)$ average time complexity for storing and retrieving URLs.
* **Stack:** (In `history_module.py`) Used for the "Undo" feature. Since we need to revert the *most recent* action first, a Last-In-First-Out (LIFO) structure is mathematically optimal.
* **Queue:** (In `traffic_scheduler.py`) Used for the TTL Expiry. Links are added to a FIFO queue as they are created; the oldest links reach the front first, allowing for efficient $O(1)$ cleanup.
* **Heap / Priority Queue:** (In `main_analytics.py`) Used for Top-K Trending links. A Min-Heap keeps the most-visited links at the top in $O(\log n)$ time.
* **Graph:** Used to map redirection paths from the short alias "Node" to the long URL "Node."
* **Sorting & Searching:** We utilize Merge Sort ($O(n \log n)$) to organize the history logs by timestamp for administrative reporting.

## 4. Bottlenecks
* **Memory Limit:** A single Hash Map is limited by the RAM of the server. As the system scales to billions of URLs, the memory will become a bottleneck.
* **Cleanup Latency:** If 100,000 links expire at the exact same second, the Queue processing might temporarily slow down the system.

## 5. Scalability
To resolve the bottlenecks identified in Step 4:
* **Database Sharding:** We will partition the Hash Table across multiple nodes based on the first character of the alias (e.g., Server A handles aliases starting with A-F).
* **LRU Caching:** Frequently visited "hot" links are stored in a high-speed cache to reduce the load on the primary Hash Table.
* **Distributed Processing:** The TTL Expiry Queue is moved to a separate worker service to ensure the main redirection engine remains fast.

---

## 6. Test Plan and Test Cases
* **TC1 (Fast Lookup):** Input "www.google.com" -> Get "goog12". Verify redirection to "www.google.com" is $O(1)$. (Result: Pass)
* **TC2 (Collision Handling):** Try creating a custom alias "link1" twice. Verify second attempt is blocked. (Result: Pass)
* **TC3 (Undo Logic):** Create 3 links, call `undo()`. Verify the 3rd link is removed from the database. (Result: Pass)
* **TC4 (Expiry):** Set link to expire in 2 seconds. Verify it is purged from the Hash Table after 2 seconds. (Result: Pass)

---

## 7. Complexity Analysis
| Operation | Data Structure | Time Complexity |
| :--- | :--- | :--- |
| Redirection | Hash Table | $O(1)$ |
| Undo Creation | Stack | $O(1)$ |
| Expiry Cleanup | Queue | $O(1)$ |
| Trending Analytics | Heap | $O(\log n)$ |
| History Sorting | Merge Sort | $O(n \log n)$ |

---

**Demo YouTube Video Link:** [PASTE YOUR VIDEO LINK HERE]
