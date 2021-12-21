from enum import Enum
from itertools import permutations
import math


class Node:
    def __init__(self, val=None, lc=None, rc=None):
        self.val = val
        self.lchild = lc
        self.rchild = rc

    def is_leaf(self):
        return self.val is not None


class Stream:
    def __init__(self, stream):
        self._stream = stream

    def read(self):
        head = self._stream[0]
        self._stream = self._stream[1:]
        return head

    def __len__(self):
        return len(self._stream)

    def __repr__(self):
        return str(self._stream)


def compute_parent(root, parent):
    root.parent = parent
    if root.is_leaf():
        return
    compute_parent(root.lchild, root)
    compute_parent(root.rchild, root)


def make_tree(stream):
    head = stream.read()
    if head.isdigit():
        return Node(val=int(head))

    # head is "["
    lhs = make_tree(stream)
    comma = stream.read()
    rhs = make_tree(stream)
    right_bracket = stream.read()

    return Node(val=None, lc=lhs, rc=rhs)


def make_tree_and_compute_parent(stream):
    root = make_tree(stream)
    compute_parent(root, None)
    return root


def add_tree(lhs, rhs):
    res = Node(val=None, lc=lhs, rc=rhs)
    compute_parent(res, None)
    return res


class ExplodeState(Enum):
    NOT_ENCOUNTERED = 0
    ASSGINED_LEFT = 1
    SKIPPED_SIBLING = 2
    ASSIGNED_RIGHT = 3


class SplitState(Enum):
    NOT_ENCOUTERTED = 0
    SPLITTED = 1


def explode(root, level, prev_leaf_node, state):
    if root.is_leaf():
        # print(
        #     prev_leaf_node.val if prev_leaf_node is not None else "<head>",
        #     root.val,
        #     level,
        #     state,
        # )
        if level == 5 and state == ExplodeState.NOT_ENCOUNTERED:
            if prev_leaf_node:
                prev_leaf_node.val += root.val
            state = ExplodeState.ASSGINED_LEFT
        elif state == ExplodeState.ASSGINED_LEFT:
            state = ExplodeState.SKIPPED_SIBLING
        elif state == ExplodeState.SKIPPED_SIBLING:
            root.val += prev_leaf_node.val
            prev_leaf_node.parent.val = 0
            prev_leaf_node.parent.lchild = None
            prev_leaf_node.parent.rchild = None
            state = ExplodeState.ASSIGNED_RIGHT
        return root, state
    prev_leaf_node, state = explode(root.lchild, level + 1, prev_leaf_node, state)
    prev_leaf_node, state = explode(root.rchild, level + 1, prev_leaf_node, state)
    if level == 0 and state == ExplodeState.SKIPPED_SIBLING:
        prev_leaf_node.parent.val = 0
        prev_leaf_node.parent.lchild = None
        prev_leaf_node.parent.rchild = None
    return prev_leaf_node, state


def split(root, state):
    if root.is_leaf():
        if root.val >= 10 and state == SplitState.NOT_ENCOUTERTED:
            l = math.floor(root.val / 2)
            r = math.ceil(root.val / 2)
            root.val = None
            root.lchild = Node(l)
            root.rchild = Node(r)
            root.lchild.parent = root
            root.rchild.parent = root
            state = SplitState.SPLITTED
        return state
    state = split(root.lchild, state)
    state = split(root.rchild, state)
    return state


def reduce(root):
    while True:
        # print_tree(root)
        _, explode_state = explode(root, 0, None, ExplodeState.NOT_ENCOUNTERED)
        # print(explode_state)
        if explode_state != ExplodeState.NOT_ENCOUNTERED:
            continue
        split_state = split(root, SplitState.NOT_ENCOUTERTED)
        # print(split_state)
        if split_state != SplitState.NOT_ENCOUTERTED:
            continue
        break


def print_tree(root):
    def traverse(root):
        if root.val is not None:
            return str(root.val)

        lhs = traverse(root.lchild)
        rhs = traverse(root.rchild)
        return f"[{lhs},{rhs}]"

    print(traverse(root))


def maginitude(root: Node):
    if root.is_leaf():
        return root.val
    lv = maginitude(root.lchild)
    rv = maginitude(root.rchild)
    return lv * 3 + rv * 2


with open("input.txt", "r") as fo:
    lines = fo.read().split()

mag_max = -1
for x, y in permutations(lines, 2):
    xroot = make_tree_and_compute_parent(Stream(x))
    yroot = make_tree_and_compute_parent(Stream(y))
    res = add_tree(xroot, yroot)
    reduce(res)
    mag_max = max(mag_max, maginitude(res))

print(mag_max)
