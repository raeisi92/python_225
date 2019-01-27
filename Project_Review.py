

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



#word =" MR. Mohammad is comming !!".split()
#print(sorted(word,key=len))

#from collections import defaultdict

#s1="ali reza"
#s2="ali re za"
#def anagram(s1,s2):
#    s1=s1.replace(" ","")
 #   s2=s2.replace(" ","")
    #return sorted(s1)==sorted(s2)
#print(anagram(s1,s2))
#d = defaultdict(int)
#for s in s1:
 #   ds=1


d= "محمد رئیسی"
#print(d.encode())
c= b'\xd9\x85\xd8\xad\xd9\x85\xd8\xaf \xd8\xb1\xd8\xa6\xdb\x8c\xd8\xb3\xdb\x8c'
print(c.decode())