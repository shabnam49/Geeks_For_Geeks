Given an array pre[] that represents Preorder traversal of a binary tree. One more array preLN[] is given which has only two possible values ‘L’ and ‘N’. The value ‘L’ in preLN[] indicates that the corresponding node in Binary Tree is a leaf node and value ‘N’ indicates that the corresponding node is the non-leaf node.

Note: it is a special binary tree where every node has either 0 or 2 children​

Input:
There will be T, test cases and for each test case, the function will be called separately.
The function takes three arguments as input, first, an integer N, denoting the size of both the array, second an array pre[] that represents Preorder traversal of the binary tree and the last argument a character array preLN[] which indicates that the corresponding node in Binary Tree is a leaf node or a normal node.

Output:
The output will be the inorder traversal of the resultant tree.

User Task:
Your task is to complete the function constructTree(), that constructs the tree from the given two arrays and return the root pointer to new binary tree formed.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <=T <= 100
1 <= N <= 104
1 <= pre[i] <= 107
preLN[i]: {'N', 'L'}

Example:
Input:
3
5
10 30 20 5 15 
N N L L L 
4
1 2 4 3 
N N L L 
6
1 2 4 6 5 3 
N N N L L L

Output:
20 30 5 10 15 
4 2 3 1 
6 4 5 2 3 1 

Explanation:
Testcase 1: Binary tree for the given pre array is:

The inorder traversal of given binary tree is: 20 30 5 10 15.
'''

def constructTree(pre, preLN, n):
    if(preLN==[] or pre==[]):
        return None
    if(preLN[0]=='L'):
        temp=Node(pre[0])
        pre.pop(0)
        preLN.pop(0)
        return temp
    else:
        node=Node(pre[0])
        pre.pop(0)
        preLN.pop(0)
        node.left=constructTree(pre,preLN,n)
        node.right=constructTree(pre,preLN,n)
    return node

