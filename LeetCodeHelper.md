# LeetCodeHelper
A ListNode and TreeNode helper class for LeetCode.

## ListNode.py
A leetcode ListNode helper.
1. How to use it:
    Just like the leetcode way.

2. How it helps:

    a. You can easily create a list of nodes and return the root by inputing a list, like:
``` python
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
root = List2LN(lst)
```

​	b. You can easily create a list of nodes and return the root by inputing a list, like: 

```
4->5->6->7->8->9->10->11->12->None
1->2->3->4->5->6->7->8->9->10->...
```



## TreeNode.py

A leetcode TreeNode helper.
1. How to use it:
    Just like the leetcode way.

2. How it helps:
    a. You can easily create a tree of nodes and return the root by inputing a list, like the problems in Leetcode:

    ``` python
    lst = [1,2,3,4,5,6,7,8,9,10,11,12]
            root = List2TN(lst)
    ```

    b. Change the way of representation from the default one. When you print out a Treenode, the values of itself and the left node and right node. This also works when you are debugging. The IDE would present a TreeNode like:

    ``` 
    [Self: 7]/L: 82/R: 82
    ```

    c. You can change a tree by handling the root to a list by calling the function:

    ``` python 
    lst = TN2List(root)
    ```



## Clocked_Deco.py

A decorator to get the time elapsed during runtime
how to use it:

``` python 
import Clocked_Deco

@Clocked_Deco.clock
def theFunctionYouWantToClock():
	pass
```



