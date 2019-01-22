

#t="ali","rajabi",27
#name,family,age=t
#print(name)

#from collections import defaultdict
#def get_fre(s):
#    d= defaultdict(int)
 #   for c in s:
#        d[c]+= 1
        #if  not d.get(c) is None:
            #d[c]+= 1
        #else:
            #d[c]=1
    #   return d
#print(get_fre("abbas rafte"))



N=15
p=''
import random
for i in range (N):
    p += chr(random.randint(97,122))
print(p)