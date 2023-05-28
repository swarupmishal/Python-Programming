from lib.node import Node

node_1 = Node(1)
node_2 = Node(5, node_1)

print(node_2.next.value)