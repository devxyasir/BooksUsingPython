# SECTION 8: ARRAYS AND STRINGS

---

## 8.1 Arrays — The Building Block

**Simple Explanation:**
An array is a list of items stored one after another in memory. Each item has a number (index) starting from 0.

**Deep Explanation:**
Arrays are the simplest data structure. Because items are stored contiguously, accessing by index is instant (O(1)). But inserting or deleting in the middle is slow because all later items must shift.

**Real-World Analogy:**
An array is like seats in a cinema hall. Seat 1, seat 2, seat 3... You can instantly find seat 15 by its number. But if you add a new seat in the middle, everyone after must move.

**Step-by-Step Breakdown:**
1. Create an array (list in Python).
2. Access items by index.
3. Update items by index.
4. Traversal: visit each item once.

```python
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])

# Traversal
for num in nums:
    print(num)
```

---

## 8.2 Searching

**Simple Explanation:**
Searching means finding an item in a collection. The two main methods are linear search and binary search.

**Deep Explanation:**
- **Linear Search:** Check every item one by one. O(n) time.
- **Binary Search:** Requires sorted data. Check the middle, then repeat on the correct half. O(log n) time.

**Real-World Analogy:**
Finding a word in a book. Linear search is reading every page. Binary search is opening to the middle, deciding if the word is before or after, and repeating.

```python
def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

def binary_search(items, target):
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 8.3 Sorting — Bubble and Selection

**Simple Explanation:**
Sorting means arranging items in order. Bubble sort repeatedly swaps neighbors if they are in the wrong order. Selection sort repeatedly finds the minimum and puts it in place.

**Deep Explanation:**
- **Bubble Sort:** Compare adjacent items and swap. After each pass, the largest item bubbles to the end. O(n^2).
- **Selection Sort:** Find the smallest item, swap it to the front, and repeat for the rest. O(n^2).

Both are simple but slow for large data. Better algorithms like Merge Sort and Quick Sort run in O(n log n).

**Real-World Analogy:**
Bubble sort is like lining up by height. You compare each pair of neighbors and swap if one is taller but standing behind. After one full round, the tallest is at the back.

```python
def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def selection_sort(items):
    n = len(items)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items
```

---

## 8.4 Two Pointers Technique

**Simple Explanation:**
The two pointers technique uses two indexes that move through an array to solve problems efficiently. It avoids nested loops.

**Deep Explanation:**
Instead of checking every pair with nested loops (O(n^2)), two pointers start from opposite ends or both from the start and move based on conditions (O(n)).

**Real-World Analogy:**
Two people searching a room. One starts at the left door, one at the right door. They move towards each other until they find the object.

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []
```

## Pro Tips
- Binary search only works on sorted data.
- Use two pointers for pair-finding and palindrome problems.
- Python lists are dynamic arrays with O(1) access.

## Common Mistakes
- Using binary search on unsorted data.
- Forgetting to update pointers inside a while loop.
- Off-by-one errors in index calculations.

## Interview Questions
- What is the time complexity of binary search?
- When is bubble sort a bad choice?
- Explain the two pointers technique with an example.

## Exercises
- Implement linear search on a list of names.
- Implement binary search on a sorted list.
- Find if a string is a palindrome using two pointers.
- Sort a list using bubble sort.

---

# SECTION 9: LINKED LISTS

---

## 9.1 What Is a Linked List?

**Simple Explanation:**
A linked list is a chain of nodes. Each node holds data and a link to the next node. Unlike arrays, items are not stored next to each other in memory.

**Deep Explanation:**
- **Node:** Contains `data` and `next` pointer.
- **Head:** The first node.
- **Tail:** The last node (its `next` is `None`).

Linked lists are great for insertions and deletions at the beginning. Arrays are better for random access.

**Real-World Analogy:**
A treasure hunt. You find a clue that points to the next location. Each clue (node) has a message (data) and directions to the next clue (next pointer).

**Step-by-Step Breakdown:**
1. Create a `Node` class with `data` and `next`.
2. Create a `LinkedList` class with `head`.
3. To add at front: create node, point its `next` to current head, update head.
4. To traverse: start at head, follow `next` until `None`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
```

---

## 9.2 Singly vs Doubly vs Circular

**Simple Explanation:**
- **Singly:** Each node points only to the next.
- **Doubly:** Each node points to next and previous.
- **Circular:** The last node points back to the first.

**Deep Explanation:**
- **Singly:** Uses less memory. Can only move forward.
- **Doubly:** Uses more memory. Can move both ways. Easier to delete nodes.
- **Circular:** Used for round-robin scheduling and music playlists.

**Real-World Analogy:**
A singly linked list is a one-way street. A doubly linked list is a two-way street. A circular linked list is a roundabout that loops forever.

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

## Pro Tips
- Use linked lists when you need frequent insertions/deletions at the front.
- Use arrays when you need fast access by index.
- Always check for `None` when traversing.

## Common Mistakes
- Losing the reference to the head.
- Creating infinite loops by linking a node to itself.
- Forgetting to update `next` pointers when deleting.

## Interview Questions
- What is the time complexity of inserting at the head of a linked list?
- How do you reverse a linked list?
- What are the advantages of a doubly linked list?

## Exercises
- Create a linked list and append 5 numbers.
- Write a function to count the number of nodes.
- Write a function to find the middle node.

---

# SECTION 10: STACKS AND QUEUES

---

## 10.1 Stack — Last In First Out (LIFO)

**Simple Explanation:**
A stack is like a pile of plates. You add plates on top, and you remove from the top. The last plate added is the first one removed.

**Deep Explanation:**
- **Push:** Add to the top.
- **Pop:** Remove from the top.
- **Peek:** Look at the top without removing.

Stacks use a list in Python. Append is push. Pop is pop.

**Real-World Analogy:**
A stack of books on a table. You can only take the top book. To reach the bottom book, you must remove all the books above it.

**Step-by-Step Breakdown:**
1. Create an empty list.
2. Use `.append()` to push.
3. Use `.pop()` to pop.
4. Check `len()` to see if empty.

```python
stack = []
stack.append(10)   # push
stack.append(20)
print(stack.pop())  # 20
print(stack.pop())  # 10
```

---

## 10.2 Queue — First In First Out (FIFO)

**Simple Explanation:**
A queue is like a line at a ticket counter. The first person to arrive is the first person to be served.

**Deep Explanation:**
- **Enqueue:** Add to the back.
- **Dequeue:** Remove from the front.

In Python, use `collections.deque` for efficient queues. Lists are slow for front removal.

**Real-World Analogy:**
A line at a bank. People join at the back and leave from the front. Nobody cuts the line.

**Step-by-Step Breakdown:**
1. Import `deque` from `collections`.
2. Use `.append()` to enqueue.
3. Use `.popleft()` to dequeue.

```python
from collections import deque

queue = deque()
queue.append("Ali")
queue.append("Sara")
print(queue.popleft())  # Ali
print(queue.popleft())  # Sara
```

---

## 10.3 Applications

**Simple Explanation:**
Stacks and queues are used everywhere in computing. Stacks are used for undo, browser back button, and recursion. Queues are used for printing, scheduling, and BFS.

**Deep Explanation:**
- **Stack uses:** Undo in editors, function calls, expression evaluation, backtracking.
- **Queue uses:** CPU scheduling, printer spooling, BFS in graphs, messaging systems.

**Real-World Analogy:**
Stack is like the undo button in your editor. Queue is like the line at a fast food restaurant.

```python
# Using stack for balanced parentheses
def is_balanced(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

print(is_balanced("({[]})"))
```

## Pro Tips
- Use `deque` for queues, not lists. Lists are O(n) for front removal.
- Stacks are natural for recursion and backtracking.
- Think "stack" for undo/redo and "queue" for fair scheduling.

## Common Mistakes
- Using a list for a queue with many deletions (slow).
- Forgetting to check if the stack is empty before popping.
- Confusing LIFO with FIFO in problem-solving.

## Interview Questions
- How do you implement a stack using two queues?
- What is the time complexity of push and pop in a stack?
- Where are queues used in real systems?

## Exercises
- Implement a stack with push, pop, and peek.
- Implement a queue with enqueue and dequeue.
- Check if a string has balanced brackets using a stack.

---

# SECTION 11: TREES

---

## 11.1 Binary Tree

**Simple Explanation:**
A tree is a structure where each item (node) has children. A binary tree is a tree where each node has at most two children — left and right.

**Deep Explanation:**
- **Root:** The top node.
- **Leaf:** A node with no children.
- **Height:** The longest path from root to leaf.

Trees are used for hierarchical data: file systems, organization charts, HTML DOM.

**Real-World Analogy:**
A family tree. You have a grandfather (root). He has two sons (left and right children). Each son can have their own children. People without children are leaves.

**Step-by-Step Breakdown:**
1. Create a `Node` class with `data`, `left`, and `right`.
2. Set root to None initially.
3. Build the tree by connecting nodes.

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
```

---

## 11.2 Binary Search Tree (BST)

**Simple Explanation:**
A BST is a binary tree with a special rule. Everything in the left subtree is smaller. Everything in the right subtree is larger. This makes searching very fast.

**Deep Explanation:**
- **Search:** Start at root. If target is smaller, go left. If larger, go right. O(log n) average.
- **Insert:** Find the correct spot and add. Maintain the BST rule.

**Real-World Analogy:**
A BST is like a guessing game. "I am thinking of a number between 1 and 100." You guess 50. If I say higher, you eliminate the bottom half. That is the BST rule.

```python
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.insert(data)
```

---

## 11.3 Tree Traversals

**Simple Explanation:**
Traversal means visiting every node in a tree. There are three main ways: inorder, preorder, and postorder.

**Deep Explanation:**
- **Inorder (Left, Root, Right):** Visits nodes in sorted order for BST.
- **Preorder (Root, Left, Right):** Good for copying a tree.
- **Postorder (Left, Right, Root):** Good for deleting a tree.

**Real-World Analogy:**
Inorder is like reading a book from left to right. Preorder is like announcing the chapter title before reading the pages. Postorder is like cleaning a room — you clean the corners first, then the center.

```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
```

## Pro Tips
- Inorder traversal of a BST gives sorted output.
- Use recursion for tree traversals. It is clean and natural.
- Always handle the `None` case in recursive tree functions.

## Common Mistakes
- Forgetting to check if a node is `None` before accessing children.
- Confusing inorder, preorder, and postorder.
- Not balancing a BST, leading to O(n) search in worst case.

## Interview Questions
- What is the difference between a binary tree and a BST?
- What is the time complexity of searching in a balanced BST?
- Write the inorder traversal of a binary tree.

## Exercises
- Build a BST and insert 5 numbers.
- Perform inorder, preorder, and postorder traversals.
- Calculate the height of a binary tree.

---
