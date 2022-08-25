counter = 0
temp = head

while temp:
    temp = temp.next
    counter += 1

curr = head

for i in range(counter-n-1):
    curr = curr.next

curr.next = curr.next.next
