slow = head
fast = head.next

while fast or fast.next:
    slow = slow.next
    fast = fast.next.next

second = slow.next

slow.next = None

prev = None
while second:
    temp = second.next
    second.next = prev
    prev = second
    second = temp

second = prev
first = head

while second:
    temp1 = first.next
    temp2 = second.next
    first.next = second
    second.next = temp1
    first = temp1
    second = temp2




