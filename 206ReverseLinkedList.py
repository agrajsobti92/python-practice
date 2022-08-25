cur = head
prev = None
temp = cur.next

while cur:
    cur.next = prev
    prev = cur
    cur = temp
    temp = temp.next

return prev
