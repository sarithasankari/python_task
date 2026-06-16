'''
Question: Find the first non-repeating character in a string. If no
non-repeating character exists, return None. Function Signature
def first_non_repeating(s): pass
Test Case 1 - Normal Case Input: "aabbcdde" Output: "c"
Explanation: a → repeated b → repeated c → appears once
✅ Test Case 2 - Single Character Input: "a" Output: "a"
Test Case 3 - All Characters Repeated Input: "aabbcc" Output: None
Test Case 4 - Empty String Input: "" Output: None Test Case 5 - Mixed Case
(Case Sensitive) Input: "aAbBABac" Output: "b"
'''
def first_non_repeating(s):
    g={}
    for i in s:
        if i in g:
            g[i]+=1
        else:
            g[i]=1
    for i in s:
        if g[i]==1:
            return i
    return "none"
print(first_non_repeating("aAbBABac"))
