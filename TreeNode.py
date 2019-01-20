"""
A leetcode TreeNode helper.
1. How to use it:
    Just like the leetcode way.
        
2. How it helps:
    a. You can easily create a tree of nodes and return the root by 
        inputing a list, like the problems in Leetcode:

            lst = [1,2,3,4,5,6,7,8,9,10,11,12]
            root = List2TN(lst)
    
    b. Change the way of representation from the default one. When you 
        print out a Treenode, the values of itself and the left node and 
        right node. This also works when you are debugging. The IDE 
        would present a TreeNode like:

            [Self: 7]/L: 82/R: 82
    
    c. You can change a tree by handling the root to a list by calling the 
        function:

            lst = TN2List(root)

3. Just run this file and try it out!

Versions:
- 1.0 1/19/2019 Jing Qi zzzgin@hotmail.com
    :: Created this file.
"""
class TreeNode:
    def __init__(self, x, L = None, R = None):
        self.val = x
        self.left = L
        self.right = R
    
    def __repr__(self):
        return "[Self: {0}]/L: {1}/R: {2}" \
            .format(self.val, self.left.val if self.left else None, self.right.val if self.right else None)

def List2TN(lst):
    root = TreeNode(lst[0])
    tnQ = [root]
    i = 1
    while i < len(lst):
        cur = tnQ.pop(0)
        if lst[i]!=None:
            cur.left = TreeNode(lst[i])
            tnQ.append(cur.left)
        i+=1
        if i >= len(lst):
            break
        if lst[i]!=None:
            cur.right = TreeNode(lst[i])
            tnQ.append(cur.right)
        i+=1
    return root

def TN2List(root):
    q = [root]
    r = []
    while q:
        t = q.copy()
        q.clear()
        for n in t:
            if n==None:
                r.append(None)
            else:
                r.append(n.val)
                q.append(n.left)
                q.append(n.right)
    p = len(r)-1
    while r[p]==None:
        p -= 1
    return r[:p+1]


if __name__ == "__main__":

    def test():
        l = [7,82,82,-79,98,98,-79,-79,None,-28,-24,-28,-24,None,-79,None,97,65,-4,None,3,-4,65,3,None,97]
        root = List2TN(l)
        print(root)
        lst = TN2List(root)
        print("Input and Output are the same: ", l==lst)
        pass

    test()

