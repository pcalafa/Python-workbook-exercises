# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:30:55 2021

@author: paolo
"""
'''
#extra exercise
class box:
    def db(height, width, outline = "x", fill = "."):
        if height<2 and width<2:
            print ("Error")
        print (outline*width)
        for i in range (height-2):
            print (outline + fill *(width-2)+outline)
        print (outline*width)
    def db2(height, width, outline = "@", fill = "-"):
        if height<2 and width<2:
            print ("Error")
        print (outline*width)
        for i in range (height-2):
            print (outline + fill *(width-2)+outline)
        print (outline*width)
box.db(5,5)
box.db2(7,10)
'''

'''
#Ex85

def hyp(S,s):
    h = ((S**2)+(s**2))**0.5
    print (h)
if __name__ == "__hyp__":
    hyp()
hyp(3,5)
'''

'''
#Ex86
def f(km):
    tot = 4+(0.25*((km*1000)/140))
    print ("Travel distance: "+str(km)+"km")
    print ("Taxi Fare: $"+ format((tot),'.2f'))
if __name__ == "__f__":
    f()
f(30)
'''

'''
#Ex87
def c(i):
    tot = 10.95+(i-1)*2.95
    print ("Total : $"+ format((tot),'.2f'))
if __name__ == "__c__":
    c()
c(7)    
'''

'''
#Ex88
def m(one, two , three):
    if two>one>three or three>one>two:
        median = one
    elif one>two>three or three>two>one:
        median = two
    elif one>three>two or two>three>one:
        median = three
    print (median)
if __name__ == "__m__":
    m()
m(1,2,3)    
'''    

'''
#Ex89
def i(i):
    d = {1:"one",2:"two",3:"three",4:"four",5:"five",
         6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
         11:"eleven",12:"twelve"}
    print (d.get(i))
    if i>12:
        print ("Entry error")
if __name__ == "__i__":
    i()
i(13)
'''

'''
#Ex90
def s(n):
    if 0<n<=12:
        print ("On the first day of Christmas my true love gave to me\nA song and a Christmas tree.")
        L= (list(range(2,n+1)))
        for j in L:
            l = (list(range(1,j+1)))
            print ("On the first day of Christmas my true love gave to me ")
            for i in reversed(l):
                d = {1:"A song and a Christmas tree.",2:"Two candy canes,",3:"Three boughs of holly,",4:"Four colored lights,",5:"A shining star,",
                 6:"Little silver bells,",7:"Candles a-glowing,",8:"Gold and silver tinsel,",9:"A guardian angel,",10:"Some mistletoe,",
                 11:"Gifts for one and all,",12:"All their good wishes,"}
                print (d.get(i))
    if n>12 or n==0:
        print ("Entry error")
if __name__ == "__s__":
    s()        
s(0)
'''

'''
#Ex91
def d(y,mt,d):
    lmth = (1,2,3,4,5,6,7,8,9,10,11,12)
    lMth = (1,3,5,7,8,10,12)
    lsmth = (4,6,9,11)
    lfmth = [2]
    lM = []
    lm = []
    lf = []
    if mt not in lmth:
        print ("Entry error: check month")
    elif mt in lMth and d>31:
        print ("Entry error: check day")
    elif mt in lsmth and d>30:
        print ("Entry error: check day")
    elif mt in lfmth and d>28:
        print ("Entry error: check day")
    else:
        for i in (list(range(0,mt))):
            if i == 1 or i ==3 or i ==5 or i ==7 or i ==8 or i ==10 or i ==12:
                lM.append(i)
        for j in (list(range(0,mt))):
            if j == 4 or j ==6 or j ==9 or j ==11:
                lm.append(j)
        for k in (list(range(0,mt))):
            if k == 2:
                lf.append(k)
        print (y, (len(lM)*31)+(len(lm)*30)+(len(lf)*28)+d)
if __name__ == "__d__":
    d()   
d(1980, 5, 30)
'''

'''
#Ex92
def gd(y,d):
    lmth = (31,28,31,30,31,30,31,31,30,31,30,31)
    m = list(range(1,13))
    d2 = d+280
    l=[]
    l2=[]
    l3=[]
    if y%4==0 or y%100==1 or y%400==0:
        lmth = (31,29,31,30,31,30,31,31,30,31,30,31)
    else:
        lmth = (31,28,31,30,31,30,31,31,30,31,30,31)
    for i in m:
        if d>sum(lmth[:i]):
            l.append(sum(lmth[:i]))
    if d<31:
        print (y,1,d)
    else:                
        print (y,len(l)+1,(d-(l[len(l)-1])))
    if d2<365:
        for i in m: 
            if d2>sum(lmth[:i]):
                l2.append(sum(lmth[:i]))
        print (y,len(l2)+1,(d2-(l2[len(l2)-1])))
    if 365<d2<391:
        print (y+1, 1, d2-365)
    if d2>391:
        d3 = d2-365
        for i in m:
            if d3>sum(lmth[:i]):
                l3.append(sum(lmth[:i]))
        print (y+1,len(l3)+1,(d3-(l3[len(l3)-1])))
    if y%4==0 or y%100==1 or y%400==0:
        y = "ly"
    else:
        y = "nly"
    if d>366 and y=="ly":
        print ("Wrong data entry (Leap year - days cannot be >366)")
    elif d>365 and y=="nly":
        print ("Wrong data entry (Not Leap year - days cannot be >365)")
    else:
        print ("Day entry correct")
if __name__ == "__gd__":
    gd()   
gd(1985,1)
'''

'''
#Ex93
def c(s,w):
    if w<=len(s)+1:
        print (s)
    else:
        print ("+"*w)
        print ("+"+int(((w-len(s))//2)-1)*" "+s+(int((w-len(s))/2)-1)*" "+"+")
        print ("+"*w)
s="Hello world!"
w=14    
c(s,w)
'''
'''
#Ex94
def tri(a,b,c):
    if a == 0:
        print (a>0)
        print ("one side = 0")
    elif b == 0:
        print (b>0)
        print ("one side = 0")
    elif c ==0:
        print (c>0)
        print ("one side = 0")
    elif a > c+b or b > a+c or c > a+b:
        print ("Sides are long enough")
    else:
        print ("Sides are not long enough")
    var = False
    if var:
        print ('I\'m here')
a=3
b=1
c=1
tri(a,b,c)
'''

'''
#Ex95
def cap(s):
    l=[]
    for i,j in enumerate(s):
        if j == s[0]:
            l.append(s[0].upper())
        elif s[i-2] == "?":
            l.append(s[i].upper())
        elif j == "i" and s[i-1] == " ":
            l.append(s[i].upper())
        else:
            l.append(j)
    print (s)
    print( ''.join([str(elem) for elem in l])) 
cap("what time do i have to be there? what's the address? this time i'll try to be on time")
'''

'''
#Ex96
def integer(s):
   s = s.strip()
   if (s[0] == "+" or s[0]== "-") and s[1:].isdigit():
        return True
   if s.isdigit():
        return True
   return False
def main():
    s=input("Enter a name: ")
    if integer(s):
        print ("ok")
    else:    
        print ("no")
if __name__=="__main__":     
    main()   
'''

'''
#Ex97
def op(o):
    if o == "/" or o == "*":
        print (1)
    elif o == "+" or o == "-":
        print (2)
    elif o=="^":
        print (3)
    else:
        print ("no")
def main():
    o = input("Enter operator: ")
    op(o)
if __name__=="__main__":     
    main()           
'''    

'''
#Ex98 solution from https://www.programiz.com/python-programming/examples/prime-number
def p(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")
    else:
       print(num,"is not a prime number")
def main():
    num = int(input("Enter number :"))
    p(num)
if __name__=="__main__":     
    main()

#Ex98 my solution:
def np(n):
    l=[]
    for i in range(2,n+1):
        if n%i==0:
            l.append("ok")
    if len(l)==1:
        print (str(n) +" is a prime number")
    else:
        print (str(n) +" is not a prime number")
def main():
    n = int(input("Enter a number: "))
    np(n)
if __name__=="__main__":
    main()    
'''

'''
#Ex99
def np(n):
    l=[]
    for i in range(2,n+1):
        if n%i==0:
            l.append("ok")
    if len(l)==1:
        print (str(n) +" is a prime number")
    else:
        print (str(n) +" is not a prime number")
    if len(l)!=1:
        lower = n
        upper = lower + 1000
        p=[]
        for num in range(lower,upper + 1):  
           if num > 1:  
               for i in range(2,num):  
                   if (num % i) == 0:  
                       break  
               else:  
                   p.append(num)        
        print ("the next prime number is: "+str(p[0]))
def main():
    n = int(input("Enter a number: "))
    np(n)
if __name__=="__main__":
    main()    
'''

'''
#Ex100
def r():
    import random
    ri=random.randint(7, 10)
    l=[]
    for c in (chr(i) for i in range(32,127)):
        l.append(c) 
    print(''.join(random.sample(l,ri)))
def main():
    r()
if __name__=="__main__":
   main()    
'''

'''  
#Ex101
def rego():
    import string
    import random
    tdls=[1,2,3]
    fdls=[1,2,3,4]
    tdl=[]
    tdi=[]
    fdi=[]
    for i in tdls:
        lower_upper_alphabet = string.ascii_letters.upper()
        rl = random.choice(lower_upper_alphabet)
        tdl.append(rl)
    for i in tdls:
        ri=str(random.randint(1, 9))
        tdi.append(ri)
    for i in fdls:
        ri=str(random.randint(1, 9))
        fdi.append(ri)
    old_or_new =random.randint(1, 2)
    jtl=''.join(tdl)
    jti=''.join(tdi)
    old_system=jtl+jti
    jfi=''.join(fdi)
    new_system = (jfi+jtl)
    if old_or_new == 1:
        print (old_system)
    else:
        print (new_system)
def main():
    rego()
if __name__=="__main__":
    main()   
'''

'''
#EX102
def pw():
    p = input("Enter password: ")
    lu=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    li=['0','1','2','3','4','5','6','7','8','9']
    length=[]
    upper=[]
    lower=[]
    integer=[]
    if len(p)==8:
        length.append("ok")
    for i,j in enumerate(p):
        if j in lu:
            upper.append("ok")
        if j in ll:
            lower.append("ok")
        if j in li:
            integer.append("ok")
    if len(length)==1 and len(upper)>=1 and len(lower)>=1 and len(integer)>=1:
        print ("The password you entered "+str(p)+" is correct")
    else:
        print ("The password you entered "+str(p)+" is NOT correct")
def main():
    pw()
if __name__=="__main__":
    main()
'''

'''
#EX103 (not 100% happy - can't count attempts number)
def r():#from Ex100
    global p#the password p generated inside function r, to be checked with function pw 
    import random
    ri=random.randint(8, 8)
    l=[]#empty list to be filled up with 8 ascii charachters
    for c in (chr(i) for i in range(32,127)):
        l.append(c) 
    p = (''.join(random.sample(l,ri))) #p is a string made up from joining list l items 
def pw():
    lu=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    li=['0','1','2','3','4','5','6','7','8','9']
    length=[]
    upper=[]
    lower=[]
    integer=[]
    check=[]#empty check list to get the code run until a correct password is generated
    if len(p)==8: #if password is 8 charachters long, the empty list named length will be populated with "ok"
        length.append("ok")
    for j in p: #if password has upper cases, the empty list named upper will be populated with "ok"
        if j in lu:
            upper.append("ok")
        if j in ll: #if password has lower cases, the empty list named lower will be populated with "ok"
            lower.append("ok")
        if j in li: #if password has integers, the empty list named integer will be populated with "ok"
            integer.append("ok")
    if len(length)==1 and len(upper)>=1 and len(lower)>=1 and len(integer)>=1:
        print ("The password "+str(p)+" is correct")
        check.append("y")#if check contains "y" the code stops to run (see for loop below)
    else:
        print ("The password "+str(p)+" is NOT correct")
        check.append("n")#if check contains "n" the code keeps running (see for loop below)
    for i in check:#check is a list with only one item. If item is "n", the code (r()and pw() will run again)
        if i == "n":
            r()
            pw()
        else:
            print("end")
def main():
    r()
    pw()  
if __name__=="__main__":
   main()    
'''
'''
#EX104
def hextoint():
    i = input("Enter hexadecimal int (from 0 to 9 and from A to F): ")
    l=("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F")
    n = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    if i not in l:
        print("wrong data entry")
    else:
        print([k for k,v in n.items() if v == i.upper()])
def inttohex():
    i = input("Enter base 10 int (from 0 to 15): ")
    l=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15")
    n = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    if i not in l:
        print("wrong data entry")
    else:
        print (n.get(i))
def main():
    hextoint()
    inttohex()  
if __name__=="__main__":
   main()   
'''

'''
#EX105
def base2toint():
    global n2
    i = input("Enter base2 int (from 0 to 1111): ")
    l = ("0","1","10","11","100","101","110","111","1000","1001","1010","1011","1100","1101","1110","1111")
    n2 = {"0":"0","1":"1","2":"10","3":"11","4":"100","5":"101","6":"110","7":"111","8":"1000","9":"1001","10":"1010","11":"1011","12":"1100","13":"1101","14":"1110","15":"1111"} 
    if i not in l:
        print("wrong data entry")
    else:
        print([k for k,v in n2.items() if v == i.upper()]) 
def base3toint():   
    global n3
    i = input("Enter base3 int (from 0 to 120): ")
    l=("0","1","2","10","11","12","20","21","22","100","101","102","110","111","112","120")
    n3 = {"0":"0","1":"1","2":"2","3":"10","4":"11","5":"12","6":"20","7":"21","8":"22","9":"100","10":"101","11":"102","12":"110","13":"111","14":"112","15":"120"}
    if i not in l:
        print("wrong data entry")
    else:
        print([k for k,v in n3.items() if v == i.upper()])  
def hextoint():
    global n16
    i = input("Enter hexadecimal int (from 0 to 9 and from A to F): ")
    l=("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    n16 = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    if i not in l:
        print("wrong data entry")
    else:
        print([k for k,v in n16.items() if v == i.upper()])     
def inttohex():
    i = input("Enter base 10 int (from 0 to 15): ")
    if i not in l:
        print("wrong data entry")
    else:
        print (n16.get(i))
def inttobase2():
    i = input("Enter base 10 int (from 0 to 15): ")
    if i not in l:
        print("wrong data entry")
    else:
        print (n2.get(i))
def inttobase3():
    i = input("Enter base 10 int (from 0 to 15): ")
    if i not in l:
        print("wrong data entry")
    else:
        print (n3.get(i))
def main():
    global l
    c=input("choose base: ")
    l=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15")
    if c == "2":
        c2 = input("Convert base 2 to int press 1. Convert int to base 2 press 2: ")
        if c2=="1":
            base2toint()
        if c2=="2":
            inttobase2()
        if c2!="1" and c2!="2":
            print("Wrong selection")
    if c == "3":
        c2 = input("Convert base 3 to int press 1. Convert int to base 3 press 2: ")
        if c2=="1":
            base3toint()
        if c2=="2":
            inttobase3()
        if c2!="1" and c2!="2":
            print("Wrong selection") 
    if c == "16":
        c2 = input("Convert hex to int press 1. Convert int to hex press 2: ")
        if c2=="1":
            hextoint()
        if c2=="2":
            inttohex()
        if c2!="1" and c2!="2":
            print("Wrong selection")
    if c!="2" and c!="3" and c!="16":
        print ("Base not in the options")
if __name__=="__main__":
   main()   
'''  

'''
#EX106
def m():
    y = int(input("Enter year: "))
    m = int(input("Enter month: "))
    if (m)>12:
        print("Only 12 months in a year")
    else:
        if y%4==0 or y%100==1 or y%400==0:
            lmth = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            print("the month is "+str(lmth.get(m))+" days long")
        else:
            lmth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            print("the month is "+str(lmth.get(m))+" days long")
def main():   
    m()
if __name__=="__main__":
   main()   
'''

'''
#Ex107

def d():
    n = int(input("Enter numerator: "))
    d = int(input("Enter denominator: "))
    a=[]
    if n<d:
        for i in list(range(1,n+1)):
            if n%i==0 and d%i==0 and i!=1:
                a.append(i)
    if n>d:
        for i in list(range(1,n+1)):
            if n%i==0 and d%i==0 and i!=1:
                a.append(i)
    print ("the lowest numerator is: "+str(n/a[-1])+"\nthe lowest denominator is: "+str(d/a[-1]))
def main():   
    print("~~~~~~~~~~~~~Start~~~~~~~~~~~~~~~")
    d()
    print("")
    print("~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~")
if __name__=="__main__":
   main()   
'''
'''
#Ex108
#teas=1
#tas=3*teas
#cup=16*tas
def q():
    c=int(input("Enter 1 for teaspoons\n      2 for tablespoons\n      "))
    if c==1:
        n= int(input("Enter teaspoons number: "))
        if n<3:
            print(str(n)+" teaspoons")
        if n>3 and n<3*16:
            if n%3==0:
                print(str(n//3)+" tablespoons")
            if n%3!=0:
                print(str(n//3)+" tablespoons and " +str(n-((n//3)*3))+" teaspoons")
        if n>=48:
            if n%48==0:
                print(str(n//(3*16))+" cups")
            if n%48!=0:
                if (n-((n//48)*48))<=3:
                    print(str(n//(48))+" cups and " +str(n-((n//48)*48))+" teaspoons")
                if (n-((n//48)*48))>3 and (n-((n//48)*48))<3*16:
                    print(str(n//(48))+" cups and " +str(n-((n//48)*48))+" teaspoons or")
                    print(str(n//(48))+" cups and " +str(((n-((n//48)*48))//3))+" tablespooons and "+str((n-((n//48)*48))-((n-((n//48)*48))//3)*3)+" teaspooons")
    if c==2:                
        n= int(input("Enter tablespoons number: "))
        if n<=16:
            print(str(n)+" tablespoons")
        if n>16:
            print(str(n//16)+" cups and "+str(n-((n//16)*16))+" tablespoons")
    if c!=1 and c!=2:
        print ("The number you entered is wrong")
def main(): 
    print("~~~~~~Reduce Measures~~~~~~~")
    q()
    print("~~~~~~~~~~~~End~~~~~~~~~~~~~")
if __name__=="__main__":
   main()   
'''

'''
#Ex109
def my():
    y= (list(range(1900,2000,1)))
    m= (list(range(1,13,1)))
    for i in y:
        if i%4==0 or i%100==1 or i%400==0:
            lmth = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for j in m:
                for k in lmth:
                    if k*j==(int(i)-1900):
                        print (i,j,k)
        else:
            lmth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            for j in m:
                for k in lmth:
                    if k*j==(int(i)-1900):
                        print (i,j,k)
def main():   
    my()
if __name__=="__main__":
   main()   
'''

