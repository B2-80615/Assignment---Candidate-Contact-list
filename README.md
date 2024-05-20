# Arthrex Coding Assignment 

## Problem Statement
Arthrex wants to hire an intern and maintains a database of candidates and their classmates. The goal is to list all the candidates that could be contacted until a candidate is hired or the complete list of candidates along with their classmates is exhausted.

## Approach
To solve this problem, a breadth-first search (BFS) algorithm is implemented. Starting from the given candidate, we traverse through their classmates using a queue. We mark each candidate as contacted to ensure they are not contacted more than once. This process continues until all reachable candidates are contacted.

### Queue Implementation
Implemented a custom queue using a list in Python:
```
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0```

+ __init__: Initializes an empty list to store queue items.
+ enqueue: Adds an item to the end of the queue.
+ dequeue: Removes and returns the item from the front of the queue. Returns None if the queue is empty.
+ is_empty: Checks if the queue is empty.

### Custom Set Implementation
Implemented a custom set using a dictionary in Python:
```
class CustomSet:
    def __init__(self):
        self.elements = {}

    def add(self, item):
        self.elements[item] = True

    def contains(self, item):
        return item in self.elements

    def get_all_elements(self):
        return list(self.elements.keys())```
        
+ __init__: Initializes an empty dictionary to store set elements.
+ add: Adds an item to the set.
+ contains: Checks if an item is in the set.
+ get_all_elements: Returns a list of all elements in the set.

### Friends Network Data
The friends network is represented as an adjacency list using a dictionary:
```
friends_graph = {
    'A': ['B', 'C', 'J'],
    'D': ['E', 'F', 'G'],
    'H': ['I', 'K', 'V'],
    'J': ['V'],
    'K': ['L', 'M', 'N', 'A'],
    'O': ['P', 'V', 'U'],
    'Q': ['S', 'T', 'D'],
    'U': ['H', 'J'],
    'V': ['W', 'X', 'Y', 'Z']
}```

### List All Candidates Function
This function lists all reachable friends from a given starting person using a breadth-first search algorithm:

```
def list_all_candidates(first_person):
    contacted = CustomSet()
    queue = Queue()

    # Start with the given person
    queue.enqueue(first_person)
    contacted.add(first_person)

    while not queue.is_empty():
        person = queue.dequeue()
        if person in friends_graph:
            for friend in friends_graph[person]:
                if not contacted.contains(friend):
                    contacted.add(friend)
                    queue.enqueue(friend)
    return contacted.get_all_elements() ```

+Initializes a custom set (contacted) to keep track of visited nodes and a queue (queue) for BFS.
+ Starts the traversal with the first_person.
+ Uses a while loop to process each person in the queue.
+ For each person, adds their unvisited friends to the queue and marks them as visited.

### Test Cases
Automated test cases to validate the function:
```
def test_list_all_candidates():
    # Test case 1: Starting from 'A'
    assert set(list_all_candidates('A')) == set(['A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z'])

    # Test case 2: Starting from 'D'
    assert set(list_all_candidates('D')) == set(['D', 'E', 'F', 'G'])

    # Test case 3: Starting from 'H'
    assert set(list_all_candidates('H')) == set(['H', 'I', 'K', 'V', 'L', 'M', 'N', 'A', 'B', 'C', 'J', 'W', 'X', 'Y', 'Z'])

    # Test case 4: Starting from 'M'
    assert set(list_all_candidates('M')) == set(['M'])

    # Test case 5: Starting from 'O'
    assert set(list_all_candidates('O')) == set(['O', 'P', 'V', 'U', 'W', 'X', 'Y', 'Z', 'H', 'I', 'K', 'L', 'M', 'N', 'A', 'B', 'C', 'J'])

    # Test case 6: Starting from 'Q'
    assert set(list_all_candidates('Q')) == set(['Q', 'S', 'T', 'D', 'E', 'F', 'G'])

    # Test case 7: Starting from 'U'
    assert set(list_all_candidates('U')) == set(['U', 'H', 'J', 'I', 'K', 'V', 'W', 'X', 'Y', 'Z', 'L', 'M', 'N', 'A', 'B', 'C'])

    # Test case 8: Starting from 'Z'
    assert set(list_all_candidates('Z')) == set(['Z'])

    print("All tests passed!")

if __name__ == "__main__":
    test_list_all_candidates()
```

+ Each test case starts from a different node and verifies the set of all reachable nodes.
+ If all assertions pass, it prints "All tests passed!".

### Running the Tests
To run the tests, simply execute the script:
``` python main.py ```

### Custom Test Cases
To check custom test cases interactively, you can use the following commented-out code:
```
if __name__ == "__main__":
    start_person = input("Enter the starting candidate: ").strip().upper()

    # Check if the starting person is in the graph
    if not any(start_person in friends for friends in friends_graph.values()) and start_person not in friends_graph:
        print(f"The candidate '{start_person}' is not found in the friends graph.")
    else:
        result = list_all_candidates(start_person)
        print(f"Contacted candidates starting from {start_person}: {result}") ```

This code allows you to enter a starting person interactively and lists all reachable friends.
