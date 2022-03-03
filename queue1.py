#demonstrate queue using wrapper class

class Queue():

    def __init__(self):
        self.queue = list()

    def enqueue(self, *item):
        if len(item)==1:
            self.queue.append(item)
        else:
            self.queue.extend(item)

    def dequeue(self):
        if len(self.queue)>0:
            pop_left = self.queue[0]
            del self.queue[0]
            return pop_left
        else:
            return None

    def get_len(self):
        return len(self.queue)

    def __str__(self):
        return self.queue


my_queue = Queue()

my_queue.enqueue(2,3,4,5,6)
print(my_queue.__str__())

print("\nPopped left:",my_queue.dequeue())
print("Current size of queue:",my_queue.get_len())

print("\nPopped left:",my_queue.dequeue())
print("Current size of queue:",my_queue.get_len())

print("\nPopped left:",my_queue.dequeue())
print("Current size of queue:",my_queue.get_len())

print(my_queue.__str__())
