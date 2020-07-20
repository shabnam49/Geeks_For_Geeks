'''
Given a Circular Linked List of size N. The task is to delete the given node (excluding the first and last node) in circular linked list and then print the reverse of the circular linked list.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the circular linked list. The next line contains n space separated integers forming the circular linked list. The last line contains the node to be deleted in between the circular linked list.

Output:
Print the reverse of the circular linked list with the deleted node.

Constraints:
1 <= T <= 100
1 <= n <= 100
1 <= data <= 100

Example:
Input:
2
5
2 5 7 8 10
8
4
1 7 8 10
8

Output:
10 7 5 2 
10 7 1

Explanation:
Testcase 1: After deleting 8 from the given circular linked list, it has elements as 2, 5, 7, 10. Now, reversing this list will result in 10, 7, 5, 2.
'''

void deleteNode(struct Node **head, int key)
{
    // Your code goes here
    Node* p1;
    Node* p2;
    p1 = *head;
    p2 = (*head)->next;
    while(p2->data != key)
    {
        p1 = p1->next;
        p2 = p2->next;
    }
    p1->next = p2->next;
    free(p2);
}
/* Function to reverse the linked list */
void reverse(struct Node** head)
{
Node *cur=*head,*prev=NULL,*next;
do{
next=cur->next;
cur->next=prev;
prev=cur;
cur=next;
}while(cur!=*head);
cur->next=prev;
*head=prev;
}
