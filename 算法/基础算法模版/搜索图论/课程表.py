'''
leetcode 207题: https://leetcode.com/problems/course-schedule/description/

prerequisites[i] means you have to take course prerequisites[i][1] before course prerequisites[i][0].
返回True如果可以完成所有课程，否则返回False

解题核心在于 判断有向图是否有环，如果有环则返回False，否则返回True

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        解题核心在于 判断有向图是否有环，如果有环则返回False，否则返回True
        '''
        # 建立一个字典存放有向图
        edges = {}
        # 储存每个节点/课程的入度
        indeg = [0] * numCourses

        # 将prerequisites内每个课程条件放入有向图以及入度数组。
        for info in prerequisites:
            if info[1] not in edges:
                edges[info[1]] = [info[0]]
            else:
                edges[info[1]].append(info[0])
            indeg[info[0]] += 1
            
        q = []
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        visited = 0

        while q:
            visited += 1
            u = q.pop(0)
            if u not in edges: continue
            for v in edges[u]:
                indeg[v] -= 1
                # 只有入度为0的课才会被放入queue，这样如果是有向有环图，肯定会有课是放不进queue的。那么出度数组的长度也必然会不同
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses
