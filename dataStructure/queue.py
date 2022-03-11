#demonstrate queue using Python deque

from collections import deque

my_queue = deque()

my_queue.append(2)
my_queue.append(4)
my_queue.append(6)
my_queue.append(8)
my_queue.append(10)
my_queue.append(12)

print(my_queue)

print("Popped:",my_queue.popleft())
print("Popped:",my_queue.popleft())
print("Popped:",my_queue.popleft())
print("Popped:",my_queue.popleft())
print("Popped:",my_queue.popleft())
print("Popped:",my_queue.popleft())

print(my_queue)