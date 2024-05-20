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


if __name__ == "__main__":
    start_person = input("Enter the starting candidate: ").strip().upper()

    # Check if the starting person is in the graph
    if not any(start_person in friends for friends in friends_graph.values()) and start_person not in friends_graph:
        print(f"The candidate '{start_person}' is not found in the friends graph.")
    else:
        result = list_all_candidates(start_person)
        print(f"Contacted candidates starting from {start_person}: {result}")
