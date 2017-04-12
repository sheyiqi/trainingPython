class Node(object):
    def __init__(self, data, p=0):
        self.data = data
        self.next = p
        self.pre = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            node.pre = p
            p=p.next
        return self
    
    def length(self):
        p=self.head
        i=0
        while (p.next!=0):
            i+=1
        return i
    
    def getitem(self,index):
        i=0
        p = self.head
        while (i<index):
            p=p.next
            i+=1
        if i==index:
            return p.data
    
    def insert(self, indexx, val):
        if indexx==0:
            self.head=Node(val)
        i=0
        p=self.head
        post=self.head
        while (i<indexx):
            post=p
            p=p.next
            i+=1
        if i==indexx:
            node = Node(val,p)
            post.next = node
            node.pre = post
            node.next = p
            p.pre =node
data=[1,2,3,4,5,6]
l=LinkList()
l.initlist(data)
print (l.getitem(1))
l.insert(1,12)
print (l.getitem(1))
