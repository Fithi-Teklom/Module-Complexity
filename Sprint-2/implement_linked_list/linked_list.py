
from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    __slots__ = ("value", "next", "previous")

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Node[T] | None = None
        self.previous: Node[T] | None = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def push_head(self, value: T) -> Node[T]:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self) -> T | None:
        if self.tail is None:
            return None

        value = self.tail.value
        self.remove(self.tail)
        return value

    def remove(self, node: Node[T]) -> None:
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.next = None
        node.previous = None
