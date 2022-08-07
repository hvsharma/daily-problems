# Definition for singly-linked list.

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:

  def addTwoNumbers(self, l1, l2):
    result = ListNode(0)

    return self.addNumbersRecursively(l1, l2, 0, result)

    
  def addNumbersRecursively(self, x, y, carry, result):

    if (x != None or y != None):
      addition = carry

      if (x != None):
        addition += x.val
        x = x.next

      if (y != None):
        addition += y.val
        y = y.next

      if (addition > 9):
        carry = addition // 10
        addition = addition % 10
      else:
        carry = 0
      
      result.val = addition

      if (x != None or y != None):
        result.next = self.addNumbersRecursively(x, y, carry, ListNode(0))
        
      return result
      

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print(result.val)
#   result = result.next
# 7 0 8


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(3)

l2 = ListNode(8)
l2.next = ListNode(9)
l2.next.next = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 5 2 9 9 3