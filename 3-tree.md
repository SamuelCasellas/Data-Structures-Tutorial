# Tree

A tree is similar to linked lists in that nodes are used, 
but each node points to two different nodes, one on each side. 
Nodes can be pointed to by no more than one node.

There are three main types of trees:
1. Binary Tree: Like a linked list but nodes point to two nodes, 
which has its own subtree if it doesn’t terminate into a leaf 
(a node with no child nodes).
2. BST: Data is arranged in a tree according to the size of the 
data: bigger data goes on the right, smaller data goes on the left
3. Balanced BST: An algorithm is used to assemble the data in a 
fashion where there is no more than one height difference between 
any set of leaves. One simple method that will be shown here includes 
pulling data from the middle of an ordered array first then working 
on each half. While this will not always fulfill the height difference 
requirement, this method is simple enough to examine for our purposes.

Therefore, if the data is not arranged before putting them into a tree, 
a linked list could be created unintentionally, such as by inserting data 
that is always bigger than any previous node's.

The top of every tree has a *root* node, which has no parent nodes. This 
is the first node that is referenced when traversing a tree or inserting 
data. Look at the diagram below.

![A BST has a root node and a subtree on each side of the node if the child is not a leaf node (My own image)](Picture_Files/BST.png)

In order to "dig into" the tree, recursion is needed. This essentially means
 that the method used to find/insert
the node in question is called within itself until the target destination is found.

Generally, there are no duplicates in binary trees.

# Algorithm Effeciency
Assuming that the tree is balanced, the algorithm efficiencies for the following procedures are as listed:

| Procedure | Algorithm Effeciency |
| --------- | -------------------- |
| Find node | O(log n) |
| Insert node | O(log n) |
| Traversing tree | O(n) |
| Tree.length | O(n) |

In geenral, trees are used for quick lookups of elements and perform better when compared to the linked list's
look-up time of O(n). In addition, trees are more friendly for keeping a data set sorted when inputed new data.
However, using trees can be quite cumbersome.

# Example

One great example of using a BST is keeping track of hotel rooms. Each hotel room is unique and can easily be mapped into a BST. 

In the [following example](Python_Files/Tree/hotels.py), certain rooms in a hotel are already reserved, 
whose unavailability is confirmed by the .contains_target()
method in line 24. Once the user picks a room that is
unoccupied, this room is inserted into the tree with the 
.insert_data() method in line 28.

You can find the Tree class used and its method definitions 
[here](Python_Files/Tree/tree.py).


# Problem to Solve
Now it's your turn! You will create a program that pulls from a
list of friends on your social media account. Use
[this file](Other_Files/friends_examples.txt) for an imaginary
list of friends. You will allow the user to search for a friend's name
and notify them if the list contains that name. Then print out the list of names 
and the number of friends they have.

Add an updated macro function "\_\_len\_\_" to the tree class that allows you to find the number of friends they have. Also include an "\_\_iter\_\_" macro that allows you to display the list of friends.

HINT: For the "\_\_iter\_\_" macro, you will need to use the `yield from` keyword.

Check out the solution when finished to check your work:

- [Friends solution](Python_Files/Tree/friends.py)
- [Revised Tree class](Python_Files/Tree/tree_solution.py)
