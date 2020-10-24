# 트리의 순회

import sys

def preorder(n):
    print(n.item, end="")
    if n.lf != '.':
        preorder(tree[n.lf])
    if n.rg != '.':
        preorder(tree[n.rg])

def inorder(n):
    if n.lf != '.':
        inorder(tree[n.lf])
    print(n.item, end="")
    if n.rg != '.':
        inorder(tree[n.rg])

def postorder(n):
    if n.lf != '.':
        postorder(tree[n.lf])
    if n.rg != '.':
        postorder(tree[n.rg])
    print(n.item, end="")

class Node:
    def __init__(self, item, lf, rg):
        self.item = item
        self.lf = lf
        self.rg = rg

N = int(input())
tree = {}

for n in range(N):
    data = sys.stdin.readline().split()
    tree[data[0]] = Node(item = data[0], lf = data[1], rg = data[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])