class Solution:
    def twosum(self,a,b):
        m={}
        for i in range(len(a)):
            deff=b-a[i]
            if deff in m:
                return [m[deff],a[i]]
            m[a[i]]=a[i]
        
    

a=[1,2,3,4,5,6,7,8]
b=int(input("Enter the number : "))
f=Solution()
m=f.twosum(a,b)
print(m)
