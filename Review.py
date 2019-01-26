

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

import random

#N = 10
#p=''
#l = 0
#u = 0
#c=0
#for i in range(N):
 #   if random.randint(0,61)<10:
  #      p += chr(random.randint(48,57))
    #    l+= 1
   # elif random.randint (0,1):
   #     p += chr(random.randint(65,90))
    #    u += 1
    #else:
     #   p += chr(random.randint(97,122))
      #  c += 1
#print(p)
#print(l,u,c)




#N=10
#import string
#import random
#l= string.ascii_uppercase
#u=string.ascii_lowercase
#m=string.digits
#p= random.choice (l) + random.choice(u)+ random.choice(m)
#for _ in range (N-3):
#    p += random.choice(l+u+m)
#print(p)
#l= list(p)
#random.shuffle(l)
#print("".join(l))



word =" MR. Mohammad is comming !!".split()
print(sorted(word,key=len))