def lec(p_num):
    if tree.get(p_num):
        return tree[p_num]

    p = p_num // P
    q = p_num // Q
    tree[p] = lec(p)
    tree[q] = lec(q)
    tree[p_num] = tree[p] + tree[q]
    return tree[p_num]


N, P, Q = map(int, input().split())

tree = {
    0: 1
}
lec(N)
print(tree[N])
