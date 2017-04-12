class Node(object):
    def __init__(self,data,p=0):
        self.data = data
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, index):
        if self.isempty():
            return
        if index < 0 or index > self.length():
            return
        else:
            return getitem(index)

    def getitem(self, indexx):
        if indexx < 0 or indexx > self.length() or self.empty():
            return 
        else:
            j = 0
            p = self.head
            while (j < indexx):
                p=p.next
                j+=1
            return p.data

    def length(self):
        j=0
        p=self.head
        while p != 0:
            j+=1
            p=p.next
        return j

    def empty(self):
        if self.head == 0:
            return True
        else:
            return False

    def initlist(self,array):
        self.head = Node(array[0])
        p = self.head
        for i in array[1:]:
            node = Node(i)
            p.next = node
            p = p.next
        return self

    def insert(self,indexxx,item):
        if indexxx==0:
            self.head = Node(item)
        j=0
        p=self.head
        post=self.head
        while (j<indexxx):
            post=p
            p=p.next
            j+=1
        node = Node(item,p)
        post.next = node
        node.next = p
        return self




l=LinkList()
array=[1,2,3,4,5,6]
l.initlist(array)
print (l.getitem(1))
print (l.getitem(2))
l.insert(1,10)
print (l.getitem(1))
print (l.getitem(2))
