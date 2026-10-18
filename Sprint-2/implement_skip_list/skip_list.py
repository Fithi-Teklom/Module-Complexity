
import random

class Node:
    __slots__ = ("value", "forward")

    def __init__(self, value: int, level: int) -> None:
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self) -> None:
        self.max_level = 4
        self.level = 0
        self.head = Node(0, self.max_level)
    
    def _random_level(self) -> int:
        level = 0

        while level < self.max_level and random.random() < 0.5:
            level += 1

        return level
    def insert(self, value: int) -> None:
        update = [self.head] * (self.max_level + 1)
        current = self.head

        for level in range(self.level, -1, -1):
            while current.forward[level] is not None:
                if current.forward[level].value < value:
                    current = current.forward[level]
                else:
                    break

            update[level] = current

        node_level = self._random_level()
        new_node = Node(value, node_level)
 
        if node_level > self.level:
            for i in range(self.level + 1, node_level + 1):
                update[i] = self.head
                self.level = node_level

        for i in range(node_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def contains(self, value: int | str) -> bool:
        current = self.head

        for level in range(self.level, -1, -1):
            while current.forward[level] is not None:
                if current.forward[level].value < value:
                    current = current.forward[level]
                else:
                    break

        current = current.forward[0]

        return current is not None and current.value == value

    def __contains__(self, value: int | str) -> bool:
        return self.contains(value)

    def to_list(self) -> list[int | str]:
        result = []
        current = self.head.forward[0]

        while current is not None:
            result.append(current.value)
            current = current.forward[0]

        return result