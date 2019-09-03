# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:29:22 2019

@author: Student
"""

s = 'abcdacbef'
sub_s = ''
temp = ''
i = 0
while i < len(s):
    #get all the index and s[index]
   # print(i,s[i])
    # range check
    if i+1 >= len(s) or (i+2) >= len(s):
        #print("index out of range")
        break
    else:
        #compare first two letters, if it is substring save it in temp
        if s[i] < s[i+1]:  
            sub_s = s[i:i+2]
            if len(temp) < len(sub_s):
                temp = sub_s
            #print("sub= "+sub_s)
            #find the rest substring.compare substring's last letter with next letter in the string,
            #keep concatenating the next letter to the substring 
            #until the next letter is smaller than the last letter in the substring
            j = i + 2
            # j starts from the third letter until a letter bigger than the last letter in the substring
            while j < len(s):
                if sub_s[len(sub_s)-1] <= s[j]:
                    sub_s += s[j]
                    j += 1
                   # print("new sub_s= "+sub_s)
               
                else:
                    break
               # keep track the length of substring,put the biggest substring in the temp
            if len(temp) < len(sub_s):
                temp = sub_s
            
           #next i start from the current j's position 
            i = j
        else:
            i += 1
#no substring is found in S, then longest substring is first letter
if temp == '':
    temp = s[0]
print("Longest substring in alphabetical order is "+temp)
        
       
        
            
                   
       
           
          
   