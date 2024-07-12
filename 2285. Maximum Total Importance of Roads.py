class Solution():
    def maximumImportance(self, n, roads):
        dic = {}
        for j in range(n):
            dic[j] = 0

        for i in roads:
            dic[i[0]] += 1
            dic[i[1]] += 1

        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        p = 1
        for i in dic:
            dic[i] = p
            p+=1

        total = 0
        for i in roads:
            total += dic[i[0]] + dic[i[1]]
        
        return total

obj = Solution()
print(obj.maximumImportance(5,[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
