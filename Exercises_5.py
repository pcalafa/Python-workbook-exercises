# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:06:14 2021

@author: paolo
"""
'''
#Ex110
n = int(input("Enter number: "))
l=[]
l.append(n)
while n>0:
    n = int(input("Enter number: "))
    if n>0:
        l.append(n)
    else:
        break
a= (sorted(l))
for i in a:
    print (i)
'''


'''
#Ex111
n = int(input("Enter number: "))
l=[]
l.append(n)
while n>0:
    n = int(input("Enter number: "))
    if n>0:
        l.append(n)
    else:
        break
a= (sorted(l))
for i in a[::-1]:
    print (i)
'''    


'''
#Ex112    
def k():
    global l
    n = int(input("Enter number: "))
    l=[]
    l.append(n)
    while n>0:
        n = int(input("Enter number: "))
        if n>0:
            l.append(n)
        else:
            break
def main():
    print("~~~~~~~~~Start~~~~~~~~~")
    k()    
    if len(l)<4:
        print("list is too short")
        print("~~~~~~~~~~End~~~~~~~~~~")
    else:
        a= (sorted(l))
        del a[0]
        del a[-1]
        print(a)
        print("~~~~~~~~~~End~~~~~~~~~~")
if __name__=="__main__":
    main()
'''


'''
#Ex113
n = (input("Enter word: "))
l=[]
l.append(n)
while n!="":
    n = (input("Enter word: "))
    l.append(n)
    if n=="":
        break
del l[-1]
l = list(dict.fromkeys(l))
for i in l:
    print (i)
'''


'''
#Ex114   
n = input("Enter number: ")
l=[]
l.append(n)
while n!="":
    n = input("Enter number: ")
    l.append(n)
    if n=="":
        break
del l[-1]        
l = [ int(x) for x in l]
n=[]
z=[]
p=[]
for i in l:
    if i ==0:
        z.append(i)
    elif i<0:
        n.append(i)
    else:
        p.append(i)
for i in n:
    print (i)
for i in z:
    print (i)
for i in p:
    print (i)    
'''

'''        
#Ex115    
def d(n):
    l=list(range(1,n+1))
    h=[]
    for i in l:
        if n%i==0:
            h.append(i)
    print(h)
def main():
    n=int(input("Enter n: "))
    d(n) 
if __name__=="__main__":
    main()    
'''   


'''
#Ex116 
def d(n):
    l=list(range(1,n))
    h=[]
    for i in l:
        if n%i==0:
            h.append(i)
    print("The sum of the proper divisors is "+str(sum(h)))
    print (sum(h) == n)

def e():
    l=list(range(1,10001))
    for i in l:
        m=[]
        for j in l:
            if i%j==0:
                m.append(j)
        del m[-1]
        #print(m, i, sum(m))
        if sum(m) == i:
            print(i)
def main():
    n=int(input("Enter n: "))
    d(n)
    print("The list of the perfect numbers between 1 and 10000 is:")
    e() 
if __name__=="__main__":
    main()        
'''


'''
#Ex117
def w():
    s=input("Enter sentence: ")
    l=("'","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
       "s","t","u","v","w","x","y","z"," ","A","B","C","D","E","F","G","H","I","J",
       "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    ll=[]
    for i in s:
        if i in l:
            ll.append(i)
    
    ll =(','.join(ll))
    ll =(ll.replace(',',''))
    print (ll)
def main():
    w()
if __name__=="__main__":
    main()     
'''


'''
#Ex118
def p():
    s=input("Enter sentence: ")
    characters_to_remove = ",.:;?!"
    ss=s
    for i in characters_to_remove:
        ss = ss.replace(i,'')
    a = ss.split(" ")
    b=(len(a))//2
    c = (list(range(b)))
    fh=[]
    sh=[]
    for i in c:
        fh.append(a[i])
    for i in c:
        sh.append(a[-(i-(len(a)-1))])
    if (fh[0:])==(sh):
        print ("ok")
    else:
        print ("no")
def main():
    p()
if __name__=="__main__":
    main()  
'''

'''
#Ex119  

def a():
    n = int(input("Enter number: "))
    l=[]
    l.append(n)
    while n!="":
        n = (input("Enter number: "))
        l.append(n)
        if n=="":
            break
    del l[-1]
    m=[]
    for i in l:
        m.append(int(i))
    s=[]
    a=[]
    b=[]
    for i in m:
        if i<sum(m)//len(m):
            s.append(i)
        elif i == sum(m)//len(m):
            a.append(i)
        elif i > sum(m)//len(m):
            b.append(i)
    print("The average is: "+str(sum(m)//len(m)))       
    print("List of numbers below average: "+str(s))
    print("List of numbers equal to average: "+str(a))
    print("List of numbers above average: "+str(b))
def main():
    a()
if __name__=="__main__":
    main()
'''

'''
#Ex120
def a():
    n = (input("Enter number: "))
    l=[]
    l.append(n)
    while n!="":
        n = (input("Enter number: "))
        l.append(n)
        if n=="":
            break
    del l[-1] 
    b = (str(l[:-1]))
    characters_to_remove = "[]'"
    ss=b
    for i in characters_to_remove:
        ss = ss.replace(i,'')
    print (ss +" and "+str(l[-1]))
def main():
    a()
if __name__=="__main__":
    main()
'''   


'''
#Ex121
def a():
    import random
    l=[]
    while len(l)<6:
        i=random.randint(1, 49)
        if i not in l:
            l.append(i)
    print (sorted(l))
def main():
    a()
if __name__=="__main__":
    main()    
'''

'''
#Ex122
ch = input("Enter a character: ")
c=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x",
   "y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V",
   "W","X","Y","Z")
v=("a","e","i","o","u","A","E","I","O","U")
a = ch.split(" ")
b=[]
for i in a:
    if(i[0]=='A' or i[0]=='a' or i[0]=='E' or i[0] =='e' or i[0]=='I'
     or i[0]=='i' or i[0]=='O' or i[0]=='o' or i[0]=='U' or i[0]=='u'):
        b.append(i + "way")
    elif(i[0] in c and i[1] in v ) :
        b.append(i[1:]+i[0]+"ay")
    elif(i[0] and i[1] in c and i[2] in v):
         b.append(i[2:]+i[0]+i[1]+"ay")
    elif(i[0] and i[1] and i[2] in c and i[3] in v):
         b.append(i[3:]+i[0]+i[1]+i[2]+"ay")
print (*b, sep = " ")
'''

'''
#Ex123
ch = input("Enter a character: ")
c=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
C=("B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z")
v=("a","e","i","o","u")
V=("A","E","I","O","U")
p=(".",",","!","?")
a = ch.split(" ")
b=[]
for i in a:
    if(i[0] in v):                                                            #apple
        b.append(i + "way")
    elif(i[0] in V):                                                          #Apple
        b.append(i + "way")
    elif (i[0] in v and i[-1] in p):                                          #apple,
        b.append(i[:-1] + "way"+ i[-1])
    elif i[0] in V and i[-1] in p:                                            #Apple,
        b.append(i[:-1] + "way"+ i[-1])
    elif(i[0] in c and i[1] in v):                                            #computer
        b.append(i[1:]+i[0]+"ay")
    elif(i[0] in C and i[1] in v):                                            #Computer
        b.append(i[1].upper()+i[2:]+i[0].lower()+"ay")
    elif(i[0] in c and i[1] in v and i[-1] in p):                             #computer,
        b.append(i[1:-1]+i[0]+"ay"+i[-1])
    elif(i[0] in C and i[1] in v and i[-1] in p):                             #Computer,
        b.append(i[1].upper()+i[2:-1]+i[0].lower()+"ay"+i[-1])
    elif(i[0] in c and i[1] in c and i[2] in v):                              #what
         b.append(i[2:]+i[0]+i[1]+"ay")
    elif(i[0] in C and i[1] in c and i[2] in v):                              #What     
         b.append(i[2].upper()+i[3:]+i[0].lower()+i[1]+"ay")         
    elif(i[0] in c and i[1] in c and i[2] in v and i[-1] in p):               #what,   
         b.append(i[2:-1]+i[0]+i[1]+"ay"+i[-1])
    elif(i[0] in C and i[1] in c and i[2] in v and i[-1] in p):               #What,    
         b.append(i[2].upper()+i[3:-1]+i[0].lower()+i[1]+"ay"+ i[-1])    
    elif(i[0] in c and i[1] in c and i[2] in c and i[3] in v):                #scrape  
         b.append(i[3:]+i[0]+i[1]+i[2]+"ay")
    elif(i[0] in C and i[1] in c and i[2] in c and i[3] in v):                #Scrape    
         b.append(i[3].upper()+i[4:]+i[0].lower()+i[1]+i[2]+"ay")
    elif(i[0] in c and i[1] in c and i[2] in c and i[3] in v and i[-1] in p): #scrape,    
         b.append(i[3:-1]+i[0]+i[1]+i[2]+"ay" + i[-1])
    elif(i[0] in C and i[1] in c and i[2] in c and i[3] in v and i[-1] in p): #Scrape,     
         b.append(i[3].upper()+i[4:-1]+i[0].lower()+i[1]+i[2]+"ay" + i[-1])  
print (*b, sep = " ")
'''

'''
#Ex124
import numpy as np
x = input("Enter x coordinate: ")
y = input("Enter y coordinate: ")
xl =[]
yl =[]
xl.append(x)
yl.append(y)
while x!="" and y!="":
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    xl.append(x)
    yl.append(y)
    if x == "":
        break
xli = xl[:-1]
yli = yl[:-1]
xlil=[]
ylil=[]
for i in xli:
    xlil.append(float(i))
for i in yli:
    ylil.append(float(i))
xm = np.array(xlil)
ym = np.array(ylil)
n = len(xlil)
avx = sum(xlil)/len(xlil)
avy = sum(ylil)/len(ylil)
m=((sum(xm*ym))-(((sum(xm))*(sum(ym)))/n))/((sum(xm**2))-(((sum(xm))**2)/n))
b=avy-(m*avx)
print ("y = "+str(m)+"x + "+str(b))
'''

'''
#Ex125
import random
s=("s","c","d","h")
n=("2","3","4","5","6","7","8","9","T","J","Q","K","A")
d=[]
for i in s:
 for j in n:
     d.append(i+j)
rd=[]
rii =[]
ri = random.randint(0, 51)
rii.append(ri)
while len(rii)<52:
    ri = random.randint(0, 51)
    if ri not in rii:
        rii.append(ri)
        if len(rii)>52:
            break
for i in rii:
    rd.append(d[i])
print(d)
print(rd)
'''

'''
#Ex126
import random
s=("s","c","d","h")
n=("2","3","4","5","6","7","8","9","T","J","Q","K","A")
d=[]
for i in s:
 for j in n:
     d.append(i+j)
rd=[]
rii =[]
ri = random.randint(0, 51)
rii.append(ri)
while len(rii)<52:
    ri = random.randint(0, 51)
    if ri not in rii:
        rii.append(ri)
        if len(rii)>52:
            break
for i in rii:
    rd.append(d[i])
print(d)
print(rd)
hands=[]
deal=[]
for i,j in enumerate(rd):
    hands.append(rd[i:20:4])
print(hands[:4])
print(rd[20:])
'''

'''
#Ex127
n = input("Enter n: ")
l=[]
l.append(n)
while n!="":
    n = input("Enter n: ")
    l.append(n)
    if n=="":
        break
print (l[:-1])
if len(l[:-1])==1:
    print("the list has only one item")
if len(l[:-1]) > 1:
    ll=[]
    for i in (l[:-1]):
        ll.append(int(i))
        boo=[]
    for i,j in enumerate(ll):
        if (i+1<len(ll)):
            boo.append(ll[i]<ll[i+1])
    f=[]
    for i in boo:
        if i==False:
            f.append(i)
    if len(f)>0 and f[0]==False:
        print ("the list is not sorted")
    if len(f)==0:
        print("the list is sorted")
'''


'''
Ex128
n = input("Enter n: ")
l=[]
l.append(n)
while n!="":
    n = input("Enter n: ")
    l.append(n)
    if n=="":
        break
m=[]
M=[]
e=[]
for i in (l[:-1]):
    if float(i) >3:
        M.append(i)
    elif float(i) <3:
        m.append(i)
    elif float(i)==3:
        e.append(i)
print (str(len(m))+" values <3")
print (str(len(M))+" values >3")
print (str(len(e))+" values =3")
'''


'''
#Ex129
def tokenList(s):
    s = s.replace(" ", "")
    tokens =[]
    i=0
    while i < len(s):
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or \
            s[i] == "(" or s[i]==")" or s[i] == "+" or s[i] == "-":
            tokens.append(s[i])
            i = i+1
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            while i<len(s) and s[i] >= "0" and s[i] <="9":
                num = num +s[i]
                i = i+1
            tokens.append(num)
        else:
            return[]
    return tokens
def main():
    exp= input ("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are:", tokens)
main()
'''


'''
#Ex130
def token():
    s= input("enter op: ")
    s = s.replace(" ", "")
    t = []
    i=0
    if s[0] == '-' or s[0] == '+':
        t.append('u'+s[0]+s[1:])
    else:
        t.append(s[0] + s[1:])
    u = (t[0])
    l = []
    i=0
    while i < len(u):
        if u[i] == '-' and u[i-1] == '(' or  u[i] =='+' and u[i-1] == '(' or  u[i] =='-' and u[i-1] == '/' \
                or u[i] == '+' and u[i - 1] == '/' or u[i] == '-' and u[i - 1] == '*' or u[i] == '+' and u[i - 1] == '*':
            l.append('u'+u[i])
            i = i + 1
        elif u[i] == "u" and u[i+1] == "-" or u[i] == "u" and u[i+1] == "+":
            l.append(u[i]+u[i+1])
            i = i+1
        elif u[i] == "u+" and u[i+1] == "-" or u[i] == "u+" and u[i+1] == "+":
            l.append(u[i]+u[i+1])
            i = i+1
        elif u[i] == "*" or u[i] == "/" or u[i] == "^" or \
            u[i] == "(" or u[i]==")" or u[i] == "+" or u[i] == "-":
            l.append(u[i])
            i = i+1
        elif u[i] >= "0" and u[i] <= "9":
            num = ""
            while i<len(u) and u[i] >= "0" and u[i] <="9":
                num = num +u[i]
                i = i+1
            l.append(num)
    for i,j in enumerate(l):
        if l[i] == '-' and l[i-1] == 'u-':
            del(l[i])
    print("The tokens are: "+ str(l))
def main():
    token()
if __name__ == "__main__":
    main()
'''


'''
#Ex131
def token():
    s= input("enter op: ")
    s = s.replace(" ", "")
    t = []
    i=0
    if s[0] == '-' or s[0] == '+':
        t.append('u'+s[0]+s[1:])
    else:
        t.append(s[0] + s[1:])
    u = (t[0])
    l = []
    i=0
    while i < len(u):
        if u[i] == '-' and u[i-1] == '(' or  u[i] =='+' and u[i-1] == '(' or  u[i] =='-' and u[i-1] == '/' \
                or u[i] == '+' and u[i - 1] == '/' or u[i] == '-' and u[i - 1] == '*' or u[i] == '+' and u[i - 1] == '*':
            l.append('u'+u[i])
            i = i + 1
        elif u[i] == "u" and u[i+1] == "-" or u[i] == "u" and u[i+1] == "+":
            l.append(u[i]+u[i+1])
            i = i+1
        elif u[i] == "u+" and u[i+1] == "-" or u[i] == "u+" and u[i+1] == "+":
            l.append(u[i]+u[i+1])
            i = i+1
        elif u[i] == "*" or u[i] == "/" or u[i] == "^" or \
            u[i] == "(" or u[i]==")" or u[i] == "+" or u[i] == "-":
            l.append(u[i])
            i = i+1
        elif u[i] >= "0" and u[i] <= "9":
            num = ""
            while i<len(u) and u[i] >= "0" and u[i] <="9":
                num = num +u[i]
                i = i+1
            l.append(num)
    for i,j in enumerate(l):
        if l[i] == '-' and l[i-1] == 'u-':
            del(l[i])
    print("The tokens are: "+ str(l))
    m=[]
    for i,j in enumerate(l):
    #Ex131: inizio scrittura postfix==================================================================================
        if l[i-1] == '+' or l[i-1] == '-'  or l[i-1] == '*'or l[i-1] == '/' :
            if l[i-4] == "(" and l[i-3] == "u+" or l[i-4] == "(" and  l[i-3] == "u-":
                if l[i]=='(' and l[i+1]== 'u+' or l[i]=='(' and l[i+1]== 'u-':
                    l.insert(i + 4, l[i - 1])
                    l.remove(l[i - 1])
                    m.append(l)
                else:
                    l[i - 1], l[i] = l[i], l[i - 1]
                    m.append(l)
            elif l[i-3] == "(":
                if l[i]=='(' and l[i+1]== 'u+' or l[i]=='(' and l[i+1]== 'u-':
                    l.insert(i + 4, l[i - 1])
                    l.remove(l[i - 1])
                    m.append(l)
                else:
                    l[i - 1], l[i] = l[i], l[i - 1]
                    m.append(l)
            elif l[i-3] == "u+" or l[i-3] == "u-":
                l.insert(i+4,l[i-1])
                l.remove(l[i - 1])
                m.append(l)
            elif l[i-3] == "(" and l[i+1] == ")":
                l[i - 1], l[i] = l[i], l[i - 1]
                m.append(l)
            elif len(l) ==3:
                l[i - 1], l[i] = l[i], l[i - 1]
                m.append(l)
            some extra cases not finalized start======================================================================
            elif l[i-2] == ")" and l[i] == "(":
                l.insert(-1, l[i-1])
                l[-1], l[-2] = l[-2], l[-1]
                l.remove(l[i-1])
                m.append(l)
            elif l[i-2] != ")" and l[i] == "(" and l[i+1]=='u+' or l[i-2] != ")" and l[i] == "(" and l[i+1]=='u-' or l[i-2] != ")" and l[i] == "(" and l[i+1]=='u+' or l[i-2] != ")" and l[i] == "(" and l[i+1]=='u+':
                l.insert(i+4, l[i-1])
                l.remove(l[i - 1])
                m.append(l)
    #Ex131: fine scrittura postfix====================================================================================
    print("The postfix is: "+ str(m[0]))
def main():
    token()
if __name__ == "__main__":
    main()
'''

'''
#Ex132
def token():
    s= input("enter op: ")
    s = s.replace(" ", "")
    t = []
    i=0
    if s[0] == '-' or s[0] == '+':
        t.append('u'+s[0]+s[1:])
    else:
        t.append(s[0] + s[1:])
    u = (t[0])
    l = []
    i=0
    while i < len(u):
        if u[i] == '-' and u[i-1] == '(' or  u[i] =='+' and u[i-1] == '(' or  u[i] =='-' and u[i-1] == '/' \
                or u[i] == '+' and u[i - 1] == '/' or u[i] == '-' and u[i - 1] == '*' or u[i] == '+' and u[i - 1] == '*':
            l.append('u'+u[i])
            i = i + 1
        elif u[i] == "u" and u[i+1] == "-" or u[i] == "u" and u[i+1] == "+":
            l.append(u[i]+u[i+1])
            i = i+1
        elif u[i] == "u+" and u[i+1] == "-" or u[i] == "u+" and u[i+1] == "+":
            l.append(u[i]+u[i+1])
            i = i+1
        elif u[i] == "*" or u[i] == "/" or u[i] == "^" or \
            u[i] == "(" or u[i]==")" or u[i] == "+" or u[i] == "-":
            l.append(u[i])
            i = i+1
        elif u[i] >= "0" and u[i] <= "9":
            num = ""
            while i<len(u) and u[i] >= "0" and u[i] <="9":
                num = num +u[i]
                i = i+1
            l.append(num)
    for i,j in enumerate(l):
        if l[i] == '-' and l[i-1] == 'u-':
            del(l[i])
    print("The tokens are: "+ str(l))
    m=[]
    for i,j in enumerate(l):
    #Ex131: start postfix=============================================================================================
        if l[i-1] == '+' or l[i-1] == '-'  or l[i-1] == '*'or l[i-1] == '/' :
            if l[i-4] == "(" and l[i-3] == "u+" or l[i-4] == "(" and  l[i-3] == "u-":
                if l[i]=='(' and l[i+1]== 'u+' or l[i]=='(' and l[i+1]== 'u-':
                    l.insert(i + 4, l[i - 1])
                    l.remove(l[i - 1])
                    m.append(l)
                else:
                    l[i - 1], l[i] = l[i], l[i - 1]
                    m.append(l)
            elif l[i-3] == "(":
                if l[i]=='(' and l[i+1]== 'u+' or l[i]=='(' and l[i+1]== 'u-':
                    l.insert(i + 4, l[i - 1])
                    l.remove(l[i - 1])
                    m.append(l)
                else:
                    l[i - 1], l[i] = l[i], l[i - 1]
                    m.append(l)
            elif l[i-3] == "u+" or l[i-3] == "u-":
                l.insert(i+4,l[i-1])
                l.remove(l[i - 1])
                m.append(l)
            elif l[i-3] == "(" and l[i+1] == ")":
                l[i - 1], l[i] = l[i], l[i - 1]
                m.append(l)
            elif len(l) ==3:
                l[i - 1], l[i] = l[i], l[i - 1]
                m.append(l)
            elif l[i-2] != ")" and l[i] == "(" and l[i+1]=='u+' or l[i-2] != ")" and l[i] == "(" and l[i+1]=='u-':
                l.insert(i+4, l[i-1])
                l.remove(l[i - 1])
                m.append(l)
    print("The postfix is: "+ str(m[0]))
    # Ex131: end postfix==============================================================================================
    # Ex132: start calculation========================================================================================
    import operator
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,  # use operator.div for Python 2
        '%': operator.mod,
        '^': operator.xor,}
    values=[]
    op=[]
    un=[]
    binary = ('+','-','*','/')
    unary =('u-','u+')
    p = ('(',')')
    for i in m[0]:
        if i in unary:
            u=(list(i))
            un.append(u[1])
        if i not in binary and i not in unary and i not in p:
            values.append(int(i))
        if i in binary:
            op.append(i)
    results=[]
    if len(un) == 0:
        for j in op:
            if j == '+' or j=='-' or j=='*' or j== '/':
                print("The result is: " + str(ops.get(str(op[0]))(values[0], values[1])))
    if len(un)!=0:
        for i in un:
            for j in op:
                if len(un)==2:
                    if un[0] == '-' and un[1] == '-':
                        if j=='+':
                            results.append((operator.add(values[0],values[1]))*-1)
                        if j == '-' and values[0] < values[1]:
                            results.append((operator.sub(values[0], values[1]))*(-1))
                        if j == '-' and values[0] > values[1]:
                            results.append((operator.sub(values[0], values[1]))*(-1))
                        if j == '*':
                            results.append(operator.mul(values[0], values[1]))
                        if j == '/':
                            results.append(operator.truediv(values[0], values[1]))
                if len(un)==1:
                    if l[2] == 'u-' or l[3] == 'u-':
                        if j == '+' and values[0] < values[1]:
                            results.append(operator.sub(values[0], values[1]))
                        if j == '+' and values[0] > values[1]:
                            results.append(operator.sub(values[0], values[1]))
                        if j == '-':
                            results.append(operator.add(values[0], values[1]))
                        if j == '*':
                            results.append((operator.mul(values[0], values[1]))*-1)
                        if j == '/':
                            results.append((operator.truediv(values[0], values[1]))*-1)
                    if l[0] == 'u-' or l[1] == 'u-':
                        if j == '+' and values[0] < values[1]:
                            results.append((operator.sub(values[0], values[1]))*-1)
                        if j == '+' and values[0] > values[1]:
                            results.append((operator.sub(values[0], values[1]))*-1)
                        if j == '-':
                            results.append((operator.add(values[0], values[1]))*-1)
                        if j == '*':
                            results.append((operator.mul(values[0], values[1]))*-1)
                        if j == '/':
                            results.append((operator.truediv(values[0], values[1]))*-1)
        print("The result is: " + str(results[0]))
    # Ex132: end calculation==========================================================================================
def main():
    token()
if __name__ == "__main__":
    main()
'''

'''
#Ex 133

l=input("enter list: ")
sl=input("enter list 2: ")
print (list(l))
print (list(sl))
if sl in l:
    print ("list 2 is list 1 sublist")
else:
    print ("list 2 is not list 1 sublist")
'''

'''
#Ex 134
l=input("enter list: ")
ll = list(l)
sssl=[]
for i,l in enumerate(ll):
    sl=[]
    ssl=[]
    for j,i in enumerate(ll[i:]):
        sl.append(ll[j])
        ssl.append(sl)
    for i,j in enumerate(ll):
        if i<len(ssl):
            sssl.append(ssl[i][i:])
print("the subsets are: [" + str(sssl).strip('[]')+'],[]')
'''

'''
#Ex 135 my solution
import math
en=input("Enter n:") #enter last number of the list
l=(list(range(2,int(en))))
l2=list(range(2,int(math.sqrt(int(en)))+1))
fl=[]
for i in l2:
    for j in l:
        if j%i==0 and j!=i:
            fl.append(j)
for i in fl:
    if i in l:
        l.remove(i)
print ("primes:"+str(l))

'''






 