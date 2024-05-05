class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(l,gen,index,res):
            if len(gen)==k:
                res+=[gen[:]]
                return
            for i in range(index,n):
                gen+=[l[i]]
                index+=1
                recursion(l,gen,index,res)
                #using .pop() to remove 1 element from the generated list
                gen.pop()
                # iterating from the i + 1th position to avoid repetition
                index=i+1
        l=list(range(1,n+1))
        res=[]
        recursion(l,[],0,res)
        return res
        