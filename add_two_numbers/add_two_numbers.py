"""
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }


 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
"""
# Create singly linked list


class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def addTwoNumbers(l1, l2):
    # Do a for loop over the list
    # start from the end of the list
    # and concat the integer together
    # when the integer is the same length
    #  as the len of the list
    # add the integer to the
    # list in l2.
    num1 = ""
    num2 = ""
    while l1:
        num1 = str(l1.val) + num1
        num2 = str(l2.val) + num2
        l1 = l1.next
        l2 = l2.next

    sumNumber = str(int(num1) + int(num2))
    sumNumber = sumNumber[::-1]
    print()
    newList = Node(int(sumNumber[0]))
    listHead = newList

    for num in sumNumber[0:]:
        newList.next_node = Node(num)
        newList = newList.next_node
    return listHead


l1 = Node(2)
l1.next_node = Node(4)
l1.next_node.next_node = Node(3)

l2 = Node(5)
l2.next_node = Node(6)
l2.next_node.next_node = Node(4)

result = addTwoNumbers(l1, l2)

print()

while result:
    print(result.value)
    result = result.next_node
