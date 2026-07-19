class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        #List -> Adjacency list 
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        #Calculate indegree
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neig in graph[node]:
                indegree[neig] += 1
        
        #remove the edges 
        q = []
        topo = []

        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.pop(0)
            topo.append(node)

            for neig in graph[node]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    q.append(neig)

        return [] if len(topo) != len(graph) else topo
        