# DSA-CH23-GROUP-01: System Design for URL Shortening Service
**Methodology:** Chapter 23 Five-Step Process (Hermant Jain)

## 1. Use Cases Generation
* User provides long URL -> System returns short alias.
* User sets custom alias -> System validates and stores.
* Auto-expiry of links based on TTL.

## 2. Constraints and Analysis
* **Latency:** Must achieve O(1) time for redirection.
* **Storage:** Must handle millions of entries; requires sharding for scalability.

## 3. Basic Design (DSA Coverage)
* [cite_start]**Hash Table:** Used in `url_engine.py` for O(1) mapping[cite: 19].
* [cite_start]**Stack:** Used in `history_manager.py` for LIFO undo operations[cite: 20].
* [cite_start]**Queue:** Used in `scheduler.py` for FIFO expiration processing[cite: 21].
* [cite_start]**Heap:** Used in `analytics.py` for Top-K trending links.
* [cite_start]**Graph:** Used in `url_engine.py` to map referral pathways[cite: 24].
* [cite_start]**Sorting:** Merge Sort implemented for history logs[cite: 25].

## 4. Bottlenecks
* Memory limits for the Hash Table as data scales.
* High CPU usage during massive sorting of analytics logs.

## 5. Scalability
* Sharding the database by alias prefix.
* Implementing a Cache layer to reduce Hash Table lookups.

## Team Roles
* **Mirriam Moraa (BSCCS/2025/53316):** Lead & Analytics
* **Donson Baragu (BSCCS/2025/53666):** Backend Engine
* **Andrew Clyde Otieno (BSCCS/2025/54813):** Scalability & Queues
* **Sheila Wanjigi (BSCCS/2025/52142):** QA & History Stack
