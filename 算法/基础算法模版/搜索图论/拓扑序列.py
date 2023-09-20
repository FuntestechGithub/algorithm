'''
英语：Topological sorting

有向图才会有拓扑排序，无向图没有拓扑排序。

1->2
2->3
1->3

当序列为1,2,3时，1->2->3，满足条件。此序列就是拓扑排序。（所有边都是从前指向后）

一个有效无环图也被称为拓扑图

入度：指向该节点的边的数量
出度：从该节点出发的边的数量



实际应用就是将两点视为有一条边存在，整合辺的个关系并建立起一个拓扑数组。实现构造拓扑序列我们需要用到bfs。

'''



def topSort():
    queue = []
    for i in range(1,n+1):
        if d[i]==0:
            # 入度为0的节点入队
            queue.append(i)
            res.append(i)
    while queue:
        # 3. 队头元素出队
        t = queue.pop(0)
        # 4. 有向图判断t节点是否出度为0(出度为0的点不在graph的keys中)
        if t not in graph: continue
        # 5. 循环遍历满足条件的节点入队:入度为1的节点，删掉节点t后入度变为0，所以条件为入度d[j]==1
        for j in graph[t]:
            if d[j]-1==0:
                queue.append(j)
                res.append(j)
            else:
                d[j] -= 1
    return len(res)==n    # !!!出错：如果只返回res的话，那么有环图返回的res包含的节点会小于n


# 1. 输入示例
n, m = map(int, input().split())
# 2. 初始化入度状态,默认值为0
d = [0 for i in range(n+1)]
res = []    # 存储要输出的拓扑序列
# 3. 图的存储模板
graph = {}

for i in range(m):
    a,b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
        d[b] += 1    # a到b,所以节点b的入度加1
    else:
        graph[a].append(b)
        d[b] += 1    # a到b,所以节点b的入度加1

if not topSort():
    print(-1)
else:
    for item in res:
        print(item, end=" ")
