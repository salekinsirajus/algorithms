# Implementing a hash data structure in python

class Node:
    def __init__(self, key, value, _next=None):
        self.key = key
        self.value = value
        self._next = _next

class Hash:

    def __init__(self, data=None):
        # reimplement this
        self.data = data
        self.length = len(data) if not data is None else 0

        self.MAX_LENGTH = 100
        self.container = [
            [False, Node(None, None)] for i in range(self.MAX_LENGTH)
        ]

    def __contains__(self, key):
        """If key is in the hash"""
        idx = self.__generate_hash_idx(key) 
        if not self.container[idx]:
            return False 
        else:
            node = self.container[idx][1]
            # walk over the linked list
            while node:
                if key == node.key:
                    return True
                node = node._next

        return False

    def __delitem__(self, key):
        """Remove key from the hash"""
        raise NotImplementedError

    def __generate_hash_idx(self, key):
        # for now, use a modulo based op
        return key % self.MAX_LENGTH

    def __setitem__(self, key, value):
        """add a new (or modifiy existing) item with hash[key] = value"""
        increment_length = True 
        idx = self.__generate_hash_idx(key) 
        if not self.container[idx][0]:
            # new item, this slot has not been used
            self.container[idx][0] = True
            # add a new entry at the head of the linked list
            self.container[idx][1].value = value
            self.container[idx][1].key = key 
            # add a new linked list node
            self.container[idx][1]._next = Node(None, None) 
        else:
            node = self.container[idx][1]
            while node:
                # modification to the existing key
                if node.key == key:
                    increment_length = False
                    break
                if node._next is None:
                    # add a new node here
                    node._next = Node(None, None) 
                    node = node._next
                    break
                node = node._next
            
            node.value = value
            node.key = key

        if increment_length:
            self.length += 1

    def __getitem__(self, key):
        value, found = None, False

        idx = self.__generate_hash_idx(key) 
        if self.container[idx]:
            node = self.container[idx][1]
            while node:
                if node.key == key:
                    value = node.value
                    found = True
                    break
                node = node._next

        if found:
            return value
        else:
            raise KeyError("{} not found.".format(key))

    def __len__(self):
        return self.length

    def __repr__(self):
        result = "Hash with {} items".format(self.length)

        return result
