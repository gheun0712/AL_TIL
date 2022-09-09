# 1991_트리_순회
# 2022-05-19

# 전위 순회(왼>오)
def preorder(node):
    print(node, end='')
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


# 중위 순회(왼>루트>오)
def inorder(node):
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        inorder(left)
    print(node, end='')
    if right != '.':
        inorder(right)


# 후위 순회(왼>오>루트)
def postorder(node):
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(node, end='')


N = int(input())
tree = {}
for i in range(1, N + 1):
    node, left, right = input().split()
    tree[node] = [left, right]
preorder('A');
print()
inorder('A');
print()
postorder('A');
print()
