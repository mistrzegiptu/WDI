class Node:
    def __init__(self, string=None):
        self.string = string
        self.next = None

def isAscending(str):
    for i in range(len(str)-1):
        if ord(str[i]) >= ord(str[i+1]):
            return False
        
    return True

def isDescending(str):
    for i in range(len(str)-1):
        if ord(str[i]) <= ord(str[i+1]):
            return False
        
    return True

def make_order(p):
    head = p
    ascending = []
    descending = []
    other = []
    while p.next != None:
        if isAscending(p.val):
            ascending.append(p.val)
        elif isDescending(p.val):
            descending.append(p.val)
        else:
            other.append(p.val)
        p = p.next
    p = head
    for str in ascending:
        p.val = str
        if p.next == None:
            p.next = Node("")
        p=p.next

    p.val = ""
    e = Node()
    e.next = p.next
    p.next = e
    p = p.next

    for str in other:
        p.val = str
        if p.next == None:
            p.next = Node("")
        p = p.next

    p.val = ""
    e = Node()
    e.next = p.next
    p.next = e
    p = p.next

    for str in descending:
        p.val = str
        p = p.next

    print(ascending)
    print(descending)
    print(other)
    p = head
    while(p.next != None):
        print(p.val)
        p = p.next
    return head
words = ["ala", "ola", "abel", "ula", "irys", "ewa", "sroka", "gips"]
h = Node()
he = h
for str in words:
    h.val = str
    h.next = Node()
    h = h.next
make_order(he)