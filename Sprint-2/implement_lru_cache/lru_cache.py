from linked_list import LinkedList, Node
class LruCache:
    def __init__(self, limit: int) -> None:
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit: int = limit
        self.cache: dict = {}
        self.order: LinkedList[tuple] = LinkedList()

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self.order.move_to_head(node)

        return node.value[1]
    
    def set(self, key, value) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            self.order.move_to_head(node)
            return

        node = self.order.push_head((key, value))
        self.cache[key] = node

        if len(self.cache) > self.limit:
            least_recent = self.order.pop_tail()
            del self.cache[least_recent[0]]
