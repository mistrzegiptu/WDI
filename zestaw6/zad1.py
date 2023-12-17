class Node:
    def __innit__(self, value):
        self.value = value
        self.next = None

def Contain(set, val):
    while set != None:
        if set.value == val:
            return True
        if set.value > val:
            return False
        
        set = set.next

    return False

def Insert(set, value):
    