def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
   # print(rev)
    if (s == rev): 
        return True
    return False

def is_subPalindrome(s):
    s = s[1:]
    for first_char in s:
        pos = s.rfind(first_char, 0, len(s))
        while pos != -1:
            str1 = s[:pos+1]
            if isPalindrome(str1):
                return(str1)
            pos = s.rfind(first_char,0,pos)
        s = s[1:]
    return ""

fin_ans=[]
len_strg = input()
g = input()
ans = isPalindrome(g) 
  
if ans:
    print(len(g))
    print(g) 
else: 
    for i in range(0,len(g)):
        found_str = is_subPalindrome(g)
        fin_ans.append(found_str)
        g = g[1:]
    fin_ans.sort()
    print(len(max(fin_ans, key=len)))
    print(max(fin_ans, key=len))

