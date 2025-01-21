# // Time Complexity : Exponential traversal + sorting + dfs
# // Space Complexity : Exponential for storing result, grouping and dfs path
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :No


# // Your code here along with comments explaining your approach


class Solution:
    def expand(self, s: str) -> list[str]:
        self.res = []
        groups = []
        i = 0
        while i < len(s):
            
            c = s[i]                        # character 
            g = []                          # subgroup
            
            if c == '{':
                i +=1
                while s[i] != "}":         
                    if s[i] != ',':
                        g.append(s[i])
                    i+=1
                i+=1
            else:
                g.append(s[i])
                i+=1
            groups.append(sorted(g))        # sort

        # print(groups)
        self.dfs(groups, 0, [])
    
        return self.res

    def dfs(self, groups, idx, path):
        #basecase
        if idx == len(groups):
            self.res.append("".join(path))
            return
        
        #logic
        for c in groups[idx]:
            path.append(c)                      # action

            self.dfs(groups, idx+1,path)        # recurse  

            path.pop()                          # backtrack

