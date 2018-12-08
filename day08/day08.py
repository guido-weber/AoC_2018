class Node(object):
    def __init__(self):
        self.children = []
        self.metadata = []

    @classmethod
    def parse_node(cls, data, start):
        node = Node()
        next = start + 2
        num_children, num_meta = data[start:next]
        for _ in range(num_children):
            child, next = Node.parse_node(data, next)
            node.children.append(child)
        end = next + num_meta
        node.metadata = data[next:end]
        return node, end

    def sum_meta(self):
        return sum(child.sum_meta() for child in self.children) + sum(self.metadata)

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        else:
            return sum(self.children[idx - 1].value()
                       for idx in self.metadata
                       if idx > 0 and idx <= len(self.children))


TEST = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [int(x) for x in f.read().strip().split()]
        # data = [int(x) for x in TEST.split()]
    root, end = Node.parse_node(data, 0)
    assert end == len(data)
    print("Part 1: sum of all metadata is %d" % root.sum_meta())
    print("Part 2: value for root node is %d" % root.value())
