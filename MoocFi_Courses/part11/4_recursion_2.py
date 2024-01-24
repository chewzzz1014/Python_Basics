# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    if root is None:
        return float('-inf')

    max_value = root.value

    left_max = greatest_node(root.left_child)
    if left_max > max_value:
        max_value = left_max

    right_max = greatest_node(root.right_child)
    if right_max > max_value:
        max_value = right_max

    return max_value

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))


# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    if not employee.subordinates:
        return 0

    total_subordinates = len(employee.subordinates)
    for e in employee.subordinates:
        total_subordinates += count_subordinates(e)
    return total_subordinates

class Task:
    id = 0

    def __init__(self, description, programmer, workload):
        Task.id += 1
        self.description = description
        self.programmer= programmer
        self.workload = workload
        self.finished = False
    def __str__(self):
        return f'{Task.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"NOT FINISHED" if not self.finished else "FINISHED"}'
    def is_finished(self):
        return self.finished
    def mark_finished(self):
        self.finished = True

class OrderBook:
    def __init__(self):
        self.orders = []
    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))
    def all_orders(self):
        return self.orders
    def programmers(self):
        return list(set([x.programmer for x in self.orders]))
    def mark_finished(self, id: int):
        if 1<=id<=len(self.orders):
            self.orders[id-1].mark_finished()
        else:
            raise ValueError()
    def finished_orders(self):
        return [x for x in self.orders if x.finished]
    def unfinished_orders(self):
        return [x for x in self.orders if not x.finished]
    def status_of_programmer(self, programmer: str):
        if programmer not in [x.programmer for x in self.orders]:
            raise ValueError()
        finished_tasks_workload = [x.workload for x in self.orders if x.is_finished() and x.programmer==programmer]
        unfinished_tasks_workload = [x.workload for x in self.orders if not x.is_finished() and x.programmer==programmer]

        # print(finished_tasks_workload)
        # print(unfinished_tasks_workload)

        return (len(finished_tasks_workload), len(unfinished_tasks_workload), sum(finished_tasks_workload), sum(unfinished_tasks_workload))

