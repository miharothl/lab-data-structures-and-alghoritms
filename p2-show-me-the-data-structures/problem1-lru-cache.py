class Queue:
    def __init__(self):
        self.arr = []

    def size(self):
        return len(self.arr)

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.pop(0)


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.queue = Queue()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        if key in self.cache:
            value = self.cache[key]
            self.use_operation(key, value)

            return value
        else:
            return -1

    def use_operation(self, key, value):

        if self.queue.size() >= self.capacity:
            key_to_delete = self.queue.dequeue()

        if len(self.cache.keys()) >= self.capacity:
            if key_to_delete != key:
                self.cache.pop(key_to_delete)

        self.queue.enqueue(key)
        self.cache[key] = value

        print('Queue: {}'.format(self.queue.arr))
        print('Cache: {}'.format(self.cache))

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        self.use_operation(key, value)


def test_lru_cache():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    data = our_cache.get(1)
    print("Pass: Returns: '{}'. Should return '1'.".format(data) if data == 1 else "Fail")

    data = our_cache.get(2)
    print("Pass: Returns: '{}'. Should return '2'.".format(data) if data == 2 else "Fail")

    data = our_cache.get(9)  # returns -1 because 9 is not present in the cache
    print("Pass: Returns: '{}'. Should return '-1'.".format(data) if data == -1 else "Fail")

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    data = our_cache.get(3) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print("Pass: Returns: '{}'. Should return '-1'.".format(data) if data == -1 else "Fail")


if __name__ == "__main__":
    test_lru_cache()
