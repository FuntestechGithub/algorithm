'''
要求：合并有重叠或者相邻的区间

1. 按区间左端点排序
2. 依次遍历区间，如果当前区间和所有有可能重叠或者相邻的区间，就合并

'''


segs = list()
res = list()
def merge(segs):
    global res
    # 用start和end记录当前合并区间的左右端点， 初始化都为最小值以便于加入第一个
    start, end = -(10**9+10), -(10**9+10)

    # 遍历所有区间
    for i in range(len(segs)):
        l, r = segs[i][0], segs[i][1]
        # 如果当前区间和合并区间不重叠
        if(end < l):
            # 在res不是空的前提下，将合并区间加入结果集
            if(start != -(10**9+10)):
                res.append([start, end])
            start, end =l, r
        # 如果当前区间和合并区间重叠， 新右端点为两者的最大值
        else:
            end = max(end, r)

    # 将最后一个合并区间加入结果集, 防止是空的
    if(start != -(10**9+10)):
        res.append([start, end])

def main():
    global segs, res
    n = int(input())
    for i in range(n):
        segs.append(list(map(int, input().split(" "))))
    # 按左端点排序
    segs.sort(key = lambda x : x[0])

    merge(segs)

    print(len(res))
main()

