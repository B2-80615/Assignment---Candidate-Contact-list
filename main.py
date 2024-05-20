# Custom Queue implementation using a list
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
        return len(self.items) == 0


# Custom Set implementation using a dictionary
class CustomSet:
    def __init__(self):
        self.elements = {}

    def add(self, item):
        self.elements[item] = True

    def contains(self, item):
        return item in self.elements

    def get_all_elements(self):
        return list(self.elements.keys())


# Data representing the friends network
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
}


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

    return contacted.get_all_elements()


# test cases to automate the testing
def test_list_all_candidates():
    # Test case 1: Starting from 'A'
    # Expected output: ['A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z']
    assert set(list_all_candidates('A')) == set(['A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z'])

    # Test case 2: Starting from 'D'
    # Expected output: ['D', 'E', 'F', 'G']
    assert set(list_all_candidates('D')) == set(['D', 'E', 'F', 'G'])

    # Test case 3: Starting from 'H'
    # Expected output: ['H', 'I', 'K', 'V', 'L', 'M', 'N', 'A', 'B', 'C', 'J', 'W', 'X', 'Y', 'Z']
    assert set(list_all_candidates('H')) == set(['H', 'I', 'K', 'V', 'L', 'M', 'N', 'A', 'B', 'C', 'J', 'W', 'X', 'Y', 'Z'])

    # Test case 4: Starting from 'M'
    # Expected output: ['M'] because 'M' is not connected in the graph directly
    assert set(list_all_candidates('M')) == set(['M'])

    # Test case 5: Starting from 'O'
    # Expected output: ['O', 'P', 'V', 'U', 'W', 'X', 'Y', 'Z', 'H', 'I', 'K', 'L', 'M', 'N', 'A', 'B', 'C', 'J']
    assert set(list_all_candidates('O')) == set(['O', 'P', 'V', 'U', 'W', 'X', 'Y', 'Z', 'H', 'I', 'K', 'L', 'M', 'N', 'A', 'B', 'C', 'J'])

    # Test case 6: Starting from 'Q'
    # Expected output: ['Q', 'S', 'T', 'D', 'E', 'F', 'G']
    assert set(list_all_candidates('Q')) == set(['Q', 'S', 'T', 'D', 'E', 'F', 'G'])

    # Test case 7: Starting from 'U'
    # Expected output: ['U', 'H', 'J', 'I', 'K', 'V', 'W', 'X', 'Y', 'Z', 'L', 'M', 'N', 'A', 'B', 'C']
    assert set(list_all_candidates('U')) == set(['U', 'H', 'J', 'I', 'K', 'V', 'W', 'X', 'Y', 'Z', 'L', 'M', 'N', 'A', 'B', 'C'])

    # Test case 8: Starting from 'Z'
    # Expected output: ['Z'] because 'Z' is not connected in the graph directly
    assert set(list_all_candidates('Z')) == set(['Z'])

    print("All tests passed!")

if __name__ == "__main__":
    test_list_all_candidates()

# To check Custom test cases
# if __name__ == "__main__":
#     start_person = input("Enter the starting candidate: ").strip().upper()
#
#     # Check if the starting person is in the graph
#     if not any(start_person in friends for friends in friends_graph.values()) and start_person not in friends_graph:
#         print(f"The candidate '{start_person}' is not found in the friends graph.")
#     else:
#         result = list_all_candidates(start_person)
#         print(f"Contacted candidates starting from {start_person}: {result}")
