class Solution:
    def reverseParentheses(self, s):
        stack = []
        que = []
        for i in s:
            if i == ')':
                while stack:
                    pop = stack.pop()
                    if pop == '(':
                        break     
                    else:
                        que.append(pop)
                for j in que:
                    stack.append(j)
                que = []

            else:
                stack.append(i)

        str1 = ''
        for k in stack:
            str1+=k

        return str1
