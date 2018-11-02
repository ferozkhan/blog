
class Node(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(node):
    """

    :param node:
    :return: ['root', ['left', ['left.left'], 'right']]
    """
    if node is None:
        return '#'
    return '{} {} {}'.format(node.val,
                             serialize(node.left),
                             serialize(node.right))


def deserialize(data):
    def node(vals):
        val = next(vals)
        if val == '#':
            return None
        _node = Node(val)
        _node.left = node(vals)
        _node.right = node(vals)
        return _node

    vals = iter(data.split())
    return node(vals)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
