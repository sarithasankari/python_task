'''
Task 4 : Count Word Occurrences sentence = "python is easy and python is powerful"
'''
sentence = "python is easy and python is powerful"
kk=""
mm={}
for i in sentence:
    if i!=" ":
        kk+=i
    else:
        if kk in mm:
            mm[kk]+=1
        else:
            mm[kk]=1
        kk=""
if kk:
    if kk in mm:
        mm[kk]+=1
    else:
        mm[kk]=1
        
print(mm)
        
        
