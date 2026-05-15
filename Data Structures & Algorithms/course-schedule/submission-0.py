class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        for courses, pre in prerequisites:
            print(courses, pre)
            adjMap[courses].append(pre)
        print(adjMap)
        visitSet = set()

        def dfs(courses):
            if courses in visitSet:
                return False 
            if adjMap[courses] == []:
                return True 
            visitSet.add(courses)
            for i in adjMap[courses]:
                if not dfs(i):
                    return False 
            visitSet.remove(courses)
            adjMap[courses] = []
            return True
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True