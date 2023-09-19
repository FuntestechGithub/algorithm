'''
题目链接： https://www.acwing.com/problem/content/838/

并查集的应用:
将两个集合合并
询问两个元素是否在一个集合当中

用树的形式来维护集合 （不一定是二叉树）。 每个集合用根节点的编号来表示， 每个子节点都存储下他的父节点是什么 (p[x] == x)

问题1： 如何判断一个点是个树根。 if p[x] == x
问题2： 如何求x的集合编号： while px != x: x = p[px]
问题3： 如何合并两个集合： p[x] = y （把一颗树直接办过去另外一颗树的根节点下面）

优化：当自节点找到根节点后，可以直接将一路上的其他字节点都指向根节点，这样可以减少以后的查找次数。
'''

def find(x):
    if p[x] != x:
        p[x] = find(p[x])    # 路径压缩优化，将多有子节点都指向祖宗节点；!!!注意:这里find函数的参数不能是x，因为这样递归前后函数的参数不变，会陷入死循环
    return p[x]    # ！！！出错：最后要返回的是x的父节点，而不是x

if __name__=="__main__":
    n, m = map(int, input().split())
    p = [i for i in range(n+1)]    # p[x]表示x的父节点,初始化时x的父节点是他自己

    while m:
        op, x, y = input().split()

        a = int(x)
        b = int(y)

        if op == 'M':
            p[find(a)] = find(b)    # 将a的父节点指向b的a的父节点
        else:
            if find(a) == find(b):   # 判断a和b是否在一个集合当中
                print("yes")
            else:
                print("no")
        m -= 1