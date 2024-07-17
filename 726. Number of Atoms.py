class Solution:
    def countOfAtoms(self, formula):
        dict_l = {}
        
        stack = []
        l_var = ''
        for i in range(len(formula)):
            if formula[i] == ')':
                pop_e = stack.pop()
            ''''
            if formula[i].isupper():
                l_var = formula[i]
            elif formula[i].islower():
                l_var += formula[i]

            if i != len(formula)-1:
                if formula[i+1].isupper():
                    dict_l[l_var] = 1
            else:

                if formula[i].isdigit():
                    dict_l[l_var] = int(formula[i])
            '''
        return dict_l

obj = Solution()
print(obj.countOfAtoms('H5O2'))