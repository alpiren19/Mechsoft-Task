'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''



from collections import Counter

t= 'acldm1labcdhsnd'
z = 'shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa'

def getAllSubStrings(x):
    
    allSubStrings = [''] 

  
    for i in range(0, len(x)):
       
        for k in range(0, len(x) - i):
           
            allSubStrings.append(x[k:i+k+1])

    return allSubStrings


result = getAllSubStrings(t)
result2 = getAllSubStrings(z)
list_1= []
list_2 = []
for i in result2:
    if i in result:
        list_1.append(i)

c = Counter(list_1)
for k, v in c.items(): 
    list_2.append(len(k)*(v))
list_2.sort()
print(list_2[-1])







# if __name__ == '__main__':
#     find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
 