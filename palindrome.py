class Node:
  
  def __init__(self,data):
   
     self.data = data
  
     self.next = None
  
  def is_palindrome(head):
 
       s=""
      
       while head:
      
           s += head.data
   
           head = head.next
  
       return s == s[::-1]

head = Node('M')

head.next = Node('O')

head.next.next = Node('M')


if Node.is_palindrome(head):
  
   print("palindrome")

else:
  
     print("Not palindrome")

