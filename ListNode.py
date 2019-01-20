"""
A leetcode ListNode helper.
1. How to use it:
    Just like the leetcode way.
        
2. How it helps:
    a. You can easily create a list of nodes and return the root by 
        inputing a list, like:

            lst = [1,2,3,4,5,6,7,8,9,10,11,12]
            root = List2LN(lst)
    
    b. Change the way of representation from the default one. When you 
        print out a listnode, the "list" would be printed. This also
        works when you are debugging. The IDE would present a ListNode
        like a "list" like:

            4->5->6->7->8->9->10->11->12->None
            1->2->3->4->5->6->7->8->9->10->...
    

3. Just run this file and try it out!

Versions:
- 1.0 1/19/2019 Jing Qi zzzgin@hotmail.com
    :: Created this file.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        r = ""
        t = self
        for i in range(10):
            if t is None:
                break
            r += str(t.val) + "->"
            t = t.next
        if t:
            r += "..."
        else:
            r += "None"
        return r
    
def List2LN(ip):
    head = ListNode(0)
    p = head
    for i in ip:
        nN = ListNode(i)
        p.next = nN
        p = p.next
    return head.next

def String2LN(ip):
    lip = ip[1:-1].split(",")
    for i in range(len(lip)):
        lip[i] = int(lip[i])
    return List2LN(lip)

if __name__ == "__main__":
    def test():
        st = "[1,2,3,4,5,6,7,8,9,10,11,12]"
        lst = [1,2,3,4,5,6,7,8,9,10,11,12]
        st_root = String2LN(st)
        print(st_root)
        lst_root = List2LN(lst)
        p = lst_root
        while p:
            print(p)
            p = p.next
    test()
