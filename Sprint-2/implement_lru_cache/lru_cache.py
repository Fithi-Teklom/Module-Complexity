
class Node:
    __slots__ = ("key", "value", "previous", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LruCache:
    def __init__(self, limit: int) -> None:
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit: int = limit
        self.cache: dict = {}

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.previous = self.head

    def _add_before_tail(self, node: Node) -> None:
        previous_node = self.tail.previous

        node.previous = previous_node
        node.next = self.tail

        previous_node.next = node
        self.tail.previous = node

    def _remove_node(self, node: Node) -> None:
        node.previous.next = node.next
        node.next.previous = node.previous

        node.previous = None
        node.next = None

    def _mark_recently_used(self, node: Node) -> None:
        self._remove_node(node)
        self._add_before_tail(node)

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self._mark_recently_used(node)

        return node.value

    def set(self, key, value) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._mark_recently_used(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_before_tail(node)

        if len(self.cache) > self.limit:
            least_recent_node = self.head.next
            self._remove_node(least_recent_node)
            del self.cache[least_recent_node.key]
