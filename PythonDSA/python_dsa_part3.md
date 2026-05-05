# SECTION 12: GRAPHS

---

## 12.1 What Is a Graph?

**Simple Explanation:**
A graph is a collection of nodes connected by edges. It models relationships between things.

**Deep Explanation:**
- **Node (Vertex):** A point in the graph. It represents an entity.
- **Edge:** A line connecting two nodes. It represents a relationship.
- **Directed Graph:** Edges have direction (A -> B is different from B -> A).
- **Undirected Graph:** Edges have no direction (A — B is the same as B — A).
- **Weighted Graph:** Edges have a cost or distance.
- **Cyclic Graph:** Contains at least one cycle (a path that starts and ends at the same node).
- **Acyclic Graph:** Contains no cycles.

Graphs are used for maps, social networks, web pages, and scheduling tasks. The entire internet is a giant graph where web pages are nodes and hyperlinks are edges.

**Real-World Analogy:**
A graph is like a city map. Cities are nodes. Roads are edges. Some roads are one-way (directed). Some roads have tolls (weighted). A roundabout that brings you back to the same place is a cycle.

**Step-by-Step Breakdown:**
1. Create nodes.
2. Connect nodes with edges.
3. Use adjacency lists or matrices to store the graph.
4. Traverse or search the graph.

```python
# Adjacency list representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

print(graph["A"])  # ['B', 'C']
```

---

## 12.2 Adjacency List vs Adjacency Matrix

**Simple Explanation:**
An adjacency list stores neighbors for each node. An adjacency matrix is a table showing all possible connections.

**Deep Explanation:**
- **Adjacency List:** A dictionary or list of lists. For each node, store its neighbors. Space is O(V + E). Good for sparse graphs (few edges).
- **Adjacency Matrix:** A 2D array of size V x V. `matrix[i][j] = 1` if there is an edge from i to j. Space is O(V^2). Good for dense graphs (many edges).

For most real-world problems, adjacency lists are preferred because graphs are usually sparse.

**Real-World Analogy:**
An adjacency list is like a phone's contact list. You only see people you know. An adjacency matrix is like a yearbook where every student has a page for every other student, even if they never met.

```python
# Adjacency matrix
vertices = ["A", "B", "C", "D"]
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
# A is connected to B and C
print(matrix[0])  # [0, 1, 1, 0]
```

---

## 12.3 Graph Traversals — BFS and DFS

**Simple Explanation:**
BFS explores neighbors first. DFS explores as deep as possible before backtracking.

**Deep Explanation:**
- **BFS (Breadth-First Search):** Uses a queue. Visits all neighbors at the current level before moving deeper. Good for shortest path in unweighted graphs.
- **DFS (Depth-First Search):** Uses a stack (or recursion). Explores one branch fully before switching. Good for exploring all paths and detecting cycles.

Both traversals keep a `visited` set to avoid revisiting nodes. Without it, you could loop forever in a cyclic graph.

**Real-World Analogy:**
BFS is like a flood. Water spreads to all nearby rooms before reaching deeper rooms. DFS is like a maze explorer who keeps walking until hitting a wall, then turns back.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print("BFS:")
bfs(graph, "A")
print("\nDFS:")
dfs(graph, "A")
```

---

## 12.4 Weighted Graphs and Dijkstra's Algorithm

**Simple Explanation:**
In a weighted graph, edges have costs. Dijkstra's algorithm finds the cheapest path from one node to all others.

**Deep Explanation:**
Dijkstra's algorithm works like BFS but uses a priority queue (min-heap) instead of a regular queue. It always expands the node with the smallest known distance first.

Steps:
1. Set all distances to infinity except the start node (distance 0).
2. Use a priority queue ordered by distance.
3. Pop the closest node. For each neighbor, calculate the new distance.
4. If the new distance is smaller, update it and push the neighbor into the queue.
5. Repeat until the queue is empty.

Dijkstra does not work with negative edge weights. For negative weights, use the Bellman-Ford algorithm.

**Real-World Analogy:**
You are at home and want to find the cheapest way to every friend's house. You check all roads from your house, pick the shortest one, and from there check all new roads. You always expand the shortest known route first.

```python
import heapq

def dijkstra(graph, start):
    # graph[node] = list of (neighbor, weight)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current = heapq.heappop(queue)
        if current_dist > distances[current]:
            continue
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

weighted_graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}

print(dijkstra(weighted_graph, "A"))
```

---

## 12.5 Detecting Cycles

**Simple Explanation:**
A cycle is a path that starts and ends at the same node. Detecting cycles helps prevent infinite loops.

**Deep Explanation:**
In directed graphs, you can detect cycles using DFS by tracking nodes in the current recursion stack. If you reach a node that is already in the current path, a cycle exists.

In undirected graphs, keep track of the parent node. If you visit a neighbor that is not your parent and already visited, a cycle exists.

**Real-World Analogy:**
A cycle is like a roundabout that loops forever. If you keep following directions and end up back where you started, you are stuck in a cycle.

```python
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    return False
```

## Pro Tips
- Use BFS for shortest path in unweighted graphs.
- Use DFS for cycle detection and topological sorting.
- Keep a `visited` set to avoid infinite loops.
- Use adjacency lists for sparse graphs and matrices for dense graphs.
- Dijkstra only works for non-negative weights.

## Common Mistakes
- Forgetting to mark nodes as visited.
- Using DFS when BFS is needed for shortest path.
- Not handling disconnected graphs.
- Using Dijkstra with negative weights.

## Interview Questions
- What is the difference between BFS and DFS?
- When would you use a queue vs a stack for graph traversal?
- How do you detect a cycle in a directed graph?
- What is the time complexity of Dijkstra's algorithm?
- What is the difference between adjacency list and adjacency matrix?

## Exercises
- Build a graph of 5 cities and their direct connections.
- Perform BFS and DFS starting from one city.
- Find the shortest path between two nodes using BFS.
- Implement Dijkstra's algorithm on a weighted graph of 6 nodes.
- Detect if a directed graph has a cycle.

---

# SECTION 13: RECURSION

---

## 13.1 What Is Recursion?

**Simple Explanation:**
Recursion is when a function calls itself to solve a smaller version of the same problem.

**Deep Explanation:**
Every recursive function has two parts:
- **Base case:** The simplest problem. It stops the recursion.
- **Recursive case:** The function calls itself with a smaller input.

If there is no base case, the function calls itself forever and crashes. This is called a stack overflow.

Recursion works naturally on problems that can be divided into smaller identical subproblems. Trees and graphs are naturally recursive structures.

**Real-World Analogy:**
Russian nesting dolls. You open a doll and find a smaller doll inside. You keep opening until you find the smallest doll that does not open. That smallest doll is the base case.

**Step-by-Step Breakdown:**
1. Define the base case.
2. Define how to break the problem into a smaller piece.
3. Call the function on the smaller piece.
4. Combine the results.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

## 13.2 Recursion on Arrays and Trees

**Simple Explanation:**
Recursion works naturally on problems that split into smaller pieces, like arrays and trees.

**Deep Explanation:**
- On arrays, you can recurse by moving one index at a time.
- On trees, you recurse by visiting the left and right children.
- Recursion replaces loops in many tree and graph problems.

The call stack keeps track of where to return after each recursive call. Each call gets its own copy of local variables.

**Real-World Analogy:**
A manager delegates tasks. The manager gives a task to a team lead. The team lead gives subtasks to members. When the smallest task is done, results flow back up.

```python
def sum_list(nums, index=0):
    if index == len(nums):
        return 0
    return nums[index] + sum_list(nums, index + 1)

print(sum_list([1, 2, 3, 4]))  # 10

def find_max(nums, index=0):
    if index == len(nums) - 1:
        return nums[index]
    return max(nums[index], find_max(nums, index + 1))

print(find_max([3, 1, 4, 1, 5]))  # 5
```

---

## 13.3 Divide and Conquer

**Simple Explanation:**
Divide and conquer splits a problem into smaller pieces, solves each piece, and combines the results.

**Deep Explanation:**
Classic divide and conquer algorithms:
- **Merge Sort:** Split the list in half, sort each half, then merge them.
- **Quick Sort:** Pick a pivot, put smaller items on the left and larger on the right, then recurse.
- **Binary Search:** Check the middle, then recurse on the correct half.

The pattern is always: divide, conquer, combine.

**Real-World Analogy:**
Organizing a messy room. You divide the room into sections. You clean each section separately. Then you step back and admire the whole clean room.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([5, 2, 8, 1, 9]))
```

---

## 13.4 Backtracking

**Simple Explanation:**
Backtracking tries a path. If it fails, it undoes the last step and tries a different path.

**Deep Explanation:**
Backtracking is used for puzzles, mazes, and combinatorial problems. The algorithm explores one option at a time. If it reaches a dead end, it "backtracks" to the last decision point and tries another option.

Common problems solved with backtracking:
- N-Queens
- Sudoku solver
- Maze solving
- Generating all permutations

**Real-World Analogy:**
Backtracking is like trying keys on a keyring. You try one key. If it does not fit, you put it back and try the next.

```python
def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def place_queen(row):
        if row == n:
            solutions.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                place_queen(row + 1)
                board[row][col] = '.'

    place_queen(0)
    return solutions

# Solve for 4x4 board
solutions = solve_n_queens(4)
print(f"Found {len(solutions)} solutions")
for sol in solutions:
    for row in sol:
        print(row)
    print()
```

---

## 13.5 Memoization

**Simple Explanation:**
Memoization is saving the results of recursive calls so you do not compute them again.

**Deep Explanation:**
Without memoization, recursive solutions to overlapping subproblems are extremely slow. For example, the naive recursive Fibonacci function makes exponentially many calls. With memoization, each subproblem is solved once.

You can use a dictionary or a list to store results. Top-down dynamic programming is essentially recursion plus memoization.

**Real-World Analogy:**
Memoization is like writing answers on a cheat sheet. If someone asks you the same question again, you just read from the sheet instead of solving it again.

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(50))
```

## Pro Tips
- Always define the base case first.
- Trust the recursive call. Assume it works for the smaller problem.
- Watch out for stack overflow on very deep recursion.
- Use memoization when the same subproblems repeat.
- Convert recursion to iteration if the stack depth is a concern.

## Common Mistakes
- Forgetting the base case.
- Making the recursive call with the same input (infinite loop).
- Not using memoization when the same subproblems repeat.
- Ignoring stack overflow limits on deep recursion.

## Interview Questions
- What are the two parts of every recursive function?
- What is the difference between recursion and iteration?
- When should you use memoization?
- Explain divide and conquer with an example.
- What is backtracking and where is it used?

## Exercises
- Write a recursive function to count down from n to 1.
- Write a recursive function to reverse a string.
- Write a recursive function to find the maximum number in a list.
- Draw the recursion tree for `factorial(4)`.
- Implement merge sort on a list of 10 numbers.
- Write a backtracking function to generate all permutations of a string.
- Solve Fibonacci using memoization and compare speed with naive recursion.

---

# SECTION 14: DYNAMIC PROGRAMMING

---

## 14.1 What Is Dynamic Programming?

**Simple Explanation:**
Dynamic Programming (DP) is solving a big problem by solving smaller versions first and saving the answers so you do not solve them again.

**Deep Explanation:**
DP applies when:
- The problem can be broken into overlapping subproblems.
- The optimal solution to the big problem uses optimal solutions to subproblems.

There are two approaches:
- **Top-Down (Memoization):** Recursive. Store answers as you compute them.
- **Bottom-Up (Tabulation):** Iterative. Fill a table from the smallest case up.

Bottom-up is usually faster because it avoids recursion overhead. Top-down is often more intuitive to write.

**Real-World Analogy:**
You are climbing stairs. You can take 1 or 2 steps at a time. To find how many ways to reach step 5, you first find ways to reach step 4 and step 3. You save those answers. Then you combine them. You do not re-climb from the ground every time.

**Step-by-Step Breakdown:**
1. Identify the subproblem.
2. Define the recurrence relation.
3. Create a table or memo dictionary.
4. Fill it from the base case upward.
5. The final cell is your answer.

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climb_stairs(5))  # 8
```

---

## 14.2 0/1 Knapsack Pattern

**Simple Explanation:**
You have a bag with limited weight. You have items with values and weights. Pick items to maximize value without exceeding weight.

**Deep Explanation:**
For each item, you have two choices: take it or leave it.
- If you take it, add its value and reduce remaining weight.
- If you leave it, move to the next item with the same weight.

You build a table where rows are items and columns are weights. Each cell stores the best value for that capacity.

The recurrence is:
`dp[i][w] = max(value[i] + dp[i-1][w-weight[i]], dp[i-1][w])`

**Real-World Analogy:**
Packing a suitcase for a trip. You want to pack the most valuable clothes without exceeding the airline weight limit.

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5
print(knapsack(weights, values, capacity))  # 22
```

---

## 14.3 Unbounded Knapsack and Coin Change

**Simple Explanation:**
In unbounded knapsack, you can use the same item unlimited times. Coin change is a classic example.

**Deep Explanation:**
Coin change asks: "Given coin denominations and a target amount, what is the minimum number of coins needed?" or "How many ways can you make the target amount?"

The recurrence changes slightly because you can reuse items:
`dp[w] = max(dp[w], value[i] + dp[w - weight[i]])`

**Real-World Analogy:**
A vending machine must give you change using the fewest coins possible. If you have coins of 1, 5, and 10, you would use as many 10s as possible, then 5s, then 1s.

```python
def coin_change_min(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 5, 10]
amount = 27
print(coin_change_min(coins, amount))  # 5 (10+10+5+1+1)
```

---

## 14.4 Longest Common Subsequence

**Simple Explanation:**
Given two strings, find the length of the longest sequence of characters that appears in both in the same order.

**Deep Explanation:**
Compare the last characters of both strings.
- If they match, add 1 and move both back.
- If they do not match, take the better of skipping one character from either string.

This is a classic 2D DP problem. The table is (len(text1)+1) by (len(text2)+1).

**Real-World Analogy:**
Two friends write down their favorite movies. You want to find the longest list of movies they both like in the same order.

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(lcs("abcde", "ace"))  # 3
```

---

## 14.5 Longest Increasing Subsequence

**Simple Explanation:**
Find the longest subsequence where each number is larger than the previous one.

**Deep Explanation:**
For each element, check all previous elements. If the current element is larger, the sequence can be extended.

`dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]`

**Real-World Analogy:**
Planning your career. Each job should be better than the last. You want the longest chain of improving jobs.

```python
def lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
```

## Pro Tips
- Start with a recursive solution. Then add memoization.
- Look for overlapping subproblems. That is the signal to use DP.
- Practice the knapsack and LCS patterns. They appear in many disguises.
- Bottom-up is usually more memory-efficient if you only need the previous row.

## Common Mistakes
- Trying to guess the recurrence relation without writing small examples first.
- Off-by-one errors in table dimensions.
- Forgetting that bottom-up needs base cases initialized.
- Confusing subsequence with substring (subsequence does not need to be contiguous).

## Interview Questions
- What is the difference between memoization and tabulation?
- What are the properties a problem must have for DP to apply?
- Explain the knapsack problem in your own words.
- What is the time complexity of the LCS solution?
- How would you solve coin change with unlimited coins?

## Exercises
- Solve the climbing stairs problem for n = 10.
- Solve the 0/1 knapsack with 4 items and capacity 8.
- Find the LCS of "programming" and "gaming".
- Write a bottom-up solution for the Fibonacci sequence.
- Find the longest increasing subsequence in [3, 10, 2, 1, 20].
- Write a function to find the minimum coin change for amount 15 with coins [1, 3, 5].

---

# SECTION 15: HASHING AND HASH TABLES

---

## 15.1 What Is Hashing?

**Simple Explanation:**
Hashing turns a key into a number. That number decides where the value is stored.

**Deep Explanation:**
A hash function takes input of any size and returns a fixed-size number called a hash code. The hash code is used as an index in an array. Good hash functions spread keys evenly to avoid collisions.

Properties of a good hash function:
- Deterministic: same input always gives same output.
- Fast to compute.
- Uniform distribution: spreads keys evenly across the table.
- Minimizes collisions.

Hashing makes lookup, insert, and delete operations O(1) on average.

**Real-World Analogy:**
A librarian assigns each book a shelf number based on the first letter of the title. Books starting with A go to shelf 1. This is a simple hash function. Some letters may have more books (collision), so the librarian uses a chain of books on the same shelf.

---

## 15.2 Hash Tables in DSA

**Simple Explanation:**
A hash table stores key-value pairs. It uses a hash function to find where to put each pair.

**Deep Explanation:**
- **Collision:** Two keys produce the same hash code.
- **Chaining:** Store colliding items in a linked list at that index.
- **Open Addressing:** Find the next empty slot if the target is taken. Methods include linear probing, quadratic probing, and double hashing.
- **Load Factor:** The ratio of items to slots. When it exceeds a threshold (usually 0.75), the table is resized (rehashed) to maintain performance.

Python dictionaries are built on hash tables. Understanding them helps you use them correctly and debug performance issues.

**Real-World Analogy:**
A coat check at a theater. You hand over your coat. The attendant gives you a ticket with a number. Later, you show the ticket and instantly get your coat back. The ticket number is the hash.

```python
# Under the hood, Python dict is a hash table
phone_book = {
    "Yasir": "123-4567",
    "Sara": "987-6543"
}

print(phone_book["Yasir"])  # instant lookup
```

---

## 15.3 Collision Resolution

**Simple Explanation:**
When two keys land in the same spot, we need a strategy to handle it.

**Deep Explanation:**
- **Separate Chaining:** Each bucket is a linked list. All colliding keys go into the same bucket. Simple but uses extra memory for pointers.
- **Linear Probing:** If the slot is taken, try the next slot, then the next, until finding an empty one.
- **Quadratic Probing:** Try slots at increasing intervals (1, 4, 9, 16...) to reduce clustering.
- **Double Hashing:** Use a second hash function to calculate the step size.

Python's dict uses open addressing with a combination of probing and resizing.

**Real-World Analogy:**
Linear probing is like parking. You drive to your assigned spot. If it is taken, you keep driving forward until you find an empty space. Separate chaining is like a parking lot where each spot can hold a stack of cars.

---

## 15.4 Applications of Hashing

**Simple Explanation:**
Hashing is used for fast lookups, counting, and detecting duplicates.

**Deep Explanation:**
Common uses:
- **Frequency counting:** Count how many times each item appears.
- **Two-sum problem:** Check if a complement exists in O(1).
- **Caching:** Store expensive function results for reuse.
- **Hash maps vs hash sets:** Maps store key-value pairs. Sets store only keys.
- **Consistent Hashing:** Used in distributed systems to assign data to servers evenly.

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

---

## 15.5 Python Dictionary Internals

**Simple Explanation:**
Python dictionaries are highly optimized hash tables.

**Deep Explanation:**
- Dictionaries preserve insertion order since Python 3.7 (as a language guarantee).
- They use a compact, resizable array with open addressing.
- Lookups are O(1) average case.
- Keys must be hashable (immutable types like strings, numbers, tuples).
- Custom objects can be used as keys if they implement `__hash__` and `__eq__`.

**Real-World Analogy:**
A Python dictionary is like a modern smart warehouse. It knows exactly where every box is. It reorganizes itself when it gets too full. It remembers the order boxes arrived.

```python
# Dictionary comprehension
word_count = {"apple": 3, "banana": 2}

# Merging dictionaries
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = {**dict1, **dict2}
print(merged)

# Default values with get
print(word_count.get("cherry", 0))  # 0
```

## Pro Tips
- Use hash tables when you need fast lookup by key.
- Know that worst-case hash table performance is O(n) if many collisions happen.
- Immutable types (strings, numbers, tuples) can be keys. Lists cannot.
- Understand your language's hash table implementation for debugging.

## Common Mistakes
- Using a list as a dictionary key.
- Assuming dictionaries keep insertion order in very old Python versions (before 3.7).
- Not handling key errors with `.get()`.
- Forgetting that `set()` operations are faster than list operations for membership.

## Interview Questions
- What is a collision and how is it handled?
- Why are hash table lookups O(1)?
- What types can be used as dictionary keys?
- What is the difference between a hash set and a hash map?
- Explain separate chaining vs open addressing.

## Exercises
- Count the frequency of each letter in a string using a dictionary.
- Find the first non-repeating character in a string.
- Check if two lists have any common element using a set.
- Implement a simple hash table with separate chaining.
- Write a function that finds duplicates in a list using a set.

---

# SECTION 16: HEAPS AND PRIORITY QUEUES

---

## 16.1 What Is a Heap?

**Simple Explanation:**
A heap is a tree where the parent is always smaller (or larger) than its children.

**Deep Explanation:**
- **Min-Heap:** The smallest item is always at the top (root).
- **Max-Heap:** The largest item is always at the top.
- Heaps are usually implemented as binary trees stored in arrays.
- Insert and delete operations take O(log n).
- Finding the min or max takes O(1).
- Building a heap from an array takes O(n) using the heapify process.

Heaps are complete binary trees. Every level is fully filled except possibly the last, which is filled from left to right.

**Real-World Analogy:**
A hospital emergency room. The patient with the most urgent condition is treated first. The urgency is the priority. The heap keeps the most urgent patient at the top.

**Step-by-Step Breakdown:**
1. Start with an empty heap.
2. Insert pushes the item up (bubble up) until the heap rule is satisfied.
3. Extract removes the top item and pushes the last item down (bubble down).

---

## 16.2 Heapify and Heap Sort

**Simple Explanation:**
Heapify turns an array into a heap. Heap sort uses a heap to sort items in O(n log n).

**Deep Explanation:**
Heap sort steps:
1. Build a max-heap from the array.
2. Swap the root (largest) with the last item.
3. Reduce the heap size and heapify the root.
4. Repeat until the heap is empty.

Heap sort is not stable (equal elements may change order), but it is in-place and guaranteed O(n log n).

**Real-World Analogy:**
Heap sort is like repeatedly finding the tallest person in a line, moving them to the end, and then finding the next tallest among those remaining.

```python
import heapq

# Heapify an array
arr = [5, 3, 8, 1, 9]
heapq.heapify(arr)
print(arr)  # [1, 3, 8, 5, 9]

# Heap sort
def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

print(heap_sort([5, 3, 8, 1, 9]))
```

---

## 16.3 Priority Queue

**Simple Explanation:**
A priority queue is a queue where items are served based on priority, not arrival order.

**Deep Explanation:**
Python's `heapq` module implements a min-heap on a regular list.
- `heapq.heappush(heap, item)` adds an item.
- `heapq.heappop(heap)` removes the smallest item.
- For a max-heap, push negative values.

Priority queues are used in Dijkstra's algorithm, task scheduling, and simulation systems.

**Real-World Analogy:**
An airport boarding gate. First-class passengers board before economy. The priority determines order, not who arrived first.

```python
import heapq

# Min-heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 3

# Priority queue with tasks
tasks = []
heapq.heappush(tasks, (2, "write code"))
heapq.heappush(tasks, (1, "fix bug"))
heapq.heappush(tasks, (3, "test app"))

priority, task = heapq.heappop(tasks)
print(task)  # fix bug
```

---

## 16.4 Applications of Heaps

**Simple Explanation:**
Heaps are used wherever you need fast access to the smallest or largest item.

**Deep Explanation:**
- **K Largest/Smallest Elements:** Use a heap of size k.
- **Merging Sorted Lists:** Use a min-heap to track the next item from each list.
- **Median Finder:** Use two heaps (a max-heap for the lower half and a min-heap for the upper half).
- **Task Scheduling:** Always pick the highest priority task.
- **Dijkstra's Algorithm:** The priority queue is the core of the algorithm.

**Real-World Analogy:**
A heap is like a VIP lounge. No matter how many people arrive, the most important person is always at the front of the line.

```python
import heapq

def k_largest(nums, k):
    return heapq.nlargest(k, nums)

def k_smallest(nums, k):
    return heapq.nsmallest(k, nums)

print(k_largest([3, 1, 4, 1, 5, 9, 2, 6], 3))   # [9, 6, 5]
print(k_smallest([3, 1, 4, 1, 5, 9, 2, 6], 3))  # [1, 1, 2]
```

## Pro Tips
- Use `heapq` for Dijkstra's algorithm and scheduling problems.
- For max-heap, push negative values and negate on pop.
- Heaps are not good for searching arbitrary items. Use a set for that.
- `heapify` is O(n), not O(n log n). Use it when converting an existing list.

## Common Mistakes
- Trying to pop from an empty heap.
- Expecting heaps to be fully sorted. Only the top is guaranteed.
- Using a heap when a simple sorted list would be clearer.
- Forgetting that `heapq` is a min-heap by default.

## Interview Questions
- What is the difference between a heap and a binary search tree?
- What is the time complexity of inserting into a heap?
- When would you use a priority queue?
- How do you find the k largest elements in a list?
- What is heapify and why is it O(n)?

## Exercises
- Build a min-heap from a list of numbers.
- Implement a task scheduler using a priority queue.
- Find the k largest numbers in a list using a heap.
- Explain why heap sort runs in O(n log n).
- Find the median of a stream of numbers using two heaps.
- Merge k sorted lists using a heap.

---

# BONUS: THE PROGRAMMER MINDSET

---

## Thinking Like a Programmer

**Simple Explanation:**
Programming is not about memorizing code. It is about breaking problems into small, solvable pieces.

**Deep Explanation:**
When you face a hard problem:
1. Understand the problem. Write it in your own words.
2. Break it into smaller problems.
3. Solve each small problem.
4. Connect the solutions.
5. Test and improve.

This is called computational thinking. It is a skill you build with practice, not talent. The best programmers are not the ones who memorize the most syntax. They are the ones who can look at a problem, break it down, and choose the right tools.

**Real-World Analogy:**
Building a house. You do not pour the foundation, paint the walls, and install the roof at the same time. You do one step at a time. Programming is the same.

---

## How to Keep Learning

**Simple Explanation:**
Learning programming is a journey, not a destination.

**Deep Explanation:**
Technology changes constantly. New languages, frameworks, and tools appear every year. The most important skill is learning how to learn.

Strategies for continuous growth:
- Build projects. Theory without practice fades quickly.
- Read other people's code on GitHub.
- Teach what you learn. Teaching forces you to understand deeply.
- Join communities. Ask questions and help others.
- Review your old code. You will see how much you have grown.

**Real-World Analogy:**
Learning programming is like learning a musical instrument. You do not become a master by reading about music. You become a master by playing every day, making mistakes, and improving.

## Final Advice
- Do not memorize. Understand.
- Write code every day, even if it is small.
- Read other people's code to learn new styles.
- Debug patiently. Every error is a teacher.
- Keep a notebook of problems you solved and how you solved them.
- Return to basics often. Advanced concepts are just basics combined creatively.

---

Thank you for reading.
Keep learning. Keep building. Keep thinking.

**Author: Muhammad Yasir (devxyasir)**

