
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def push_head(self, value):
        # Make a new carriage
        new_node = Node(value)

        # If the train is empty, this is the first carriage
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Connect the new carriage to the old first carriage
            new_node.next = self.head
            self.head.previous = new_node

            # The new carriage is now the first carriage
            self.head = new_node

        # Give back the carriage so we can remove it later
        return new_node
    

    def pop_tail(self):
        # If the train is empty, there is nothing to remove
        if self.tail is None:
            return None

        # Remember the value we're removing
        value = self.tail.value

        # If there's only one carriage, the train becomes empty
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Move the tail backwards by one carriage
            self.tail = self.tail.previous

            # The new last carriage has no carriage after it
            self.tail.next = None

        # Return the value we removed
        return value

    def remove(self, node):
        # Connect the previous carriage to the next carriage
        if node.previous is not None:
            node.previous.next = node.next
        else:
            # There is no previous carriage, so this was the head
            self.head = node.next

        # Connect the next carriage to the previous carriage
        if node.next is not None:
            node.next.previous = node.previous
        else:
            # There is no next carriage, so this was the tail
            self.tail = node.previous

        # Disconnect the removed carriage
        node.next = None
        node.previous = None

