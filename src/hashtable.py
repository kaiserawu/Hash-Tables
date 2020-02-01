# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f'{self.key}, {self.value}, {self.next}'

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        idx = self._hash_mod(key)
        link = LinkedPair(key, value)
        if self.storage[idx] != None:
            link.next = self.storage[idx]
            self.storage[idx] = link
        else:
            self.storage[idx] = link



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        curr_entry = self.storage[idx]
        if curr_entry == None:
            print("** Warning! Key not found! **")
        else:
            if curr_entry.key == key:
                self.storage[idx] = curr_entry.next
            else:
                removed = False
                while curr_entry.next != None:
                    if curr_entry.next.key == key:
                        curr_entry.next = curr_entry.next.next
                        removed = True
                    else:
                        curr_entry = curr_entry.next
                if not removed:
                    print("** Warning! Key not found! **")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        curr_entry = self.storage[idx]
        while curr_entry != None:
            if curr_entry.key == key:
                return curr_entry.value
            else:
                curr_entry = curr_entry.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        temp_storage = self.storage[:]
        self.storage = [None] * self.capacity
        for i in range(len(temp_storage)):
            curr_entry = temp_storage[i]
            while curr_entry != None:
                self.insert(curr_entry.key, curr_entry.value)
                curr_entry = curr_entry.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
