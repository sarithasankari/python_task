'''Task 2: Remove Duplicate Values numbers = [10, 20, 30, 20, 40, 10, 50, 30] Requirements: Remove duplicates. Display unique values. Display total unique count.
Expected Output Unique Values: [10, 20, 30, 40, 50] Count: 5 '''

numbers = [10,20,30,20,40,10,50,30]
dup=[]
count=0
for i in numbers:
    if i not in dup:
        dup+=[i]
        count+=1
print("Unique Values : ",dup)
print("Count : ",count)
