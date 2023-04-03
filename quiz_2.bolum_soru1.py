class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

def count_good_nodes(node, max_val=-float('inf')):
    if not node:
        return 0
    good_nodes = 1 if node.value >= max_val else 0
    max_val = max(max_val, node.value)
    return (good_nodes + count_good_nodes(node.left, max_val) +
            count_good_nodes(node.right, max_val))

# Örnek ağacı oluşturma
root = Node(4)
root.left = Node(7)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(2)

# İyi düğüm sayısını hesaplama ve ekrana yazdırma
good_node_count = count_good_nodes(root)
print("Ağaçtaki iyi düğüm sayısı:", good_node_count)