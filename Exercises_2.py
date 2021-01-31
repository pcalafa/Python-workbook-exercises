# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:06:22 2021

@author: paolo
"""

'''
#Ex35
n = input("Enter a number: ")
if float(n)%2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")
'''

'''
#Ex36
n = input("Enter your dog's age: ")
if float(n)<=2 and float(n)>0:
    hum_age_eq = float(n)*10.5
    print ("Your dog's human equivalent age is "+ str(hum_age_eq))
elif float(n)>2:
    hum_age_eq = (float(n)-2)*4 + 2*10.5
    print ("Your dog's human equivalent age is "+ str(hum_age_eq))
elif float(n)<0:
    print ("The number you entered is incorrect")
'''

'''
#Ex37
letter = input("Enter your letter: ")
if letter =="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print ("vowel")
elif letter =="y":
    print ("vowel or consonant")
else:
    print ("consonant")
'''

'''
#Ex39
Month = input ("Enter monnth: ")
if Month =="Jan" or Month == "Mar"  or Month == "May" or Month == "Jul" or Month == "Aug" or Month == "Oct" or Month == "Dec":
    print ("31")
elif Month =="Feb":
    print ("28 or 29")
elif Month =="Apr" or Month == "Jun"  or Month == "Sep" or Month == "Nov":
    print ("30")
'''

'''
#Ex40
nl = input ("Enter noise level: ")
if float(nl) <float(40):
    print ("more quiet than in a quiet room")
elif float(nl) == float(40):
    print ("quiet room")
elif float(nl) >float(40) and float(nl)<float(70):
    print ("A far away alarm clock")
elif float(nl)==float(70):
    print ("An alarm clock")
elif float(nl) >float(70) and float(nl)< float(106):
    print ("An loud alarm clock and a far away lawnmower")
elif float(nl)==float(106):
    print ("a lawnmower")  
elif float(nl)>float(106) and float(nl)<float(130):
    print ("a far away jackhammer")
elif float(nl)==float(130):
    print ("a jackhammer")
elif float(nl)>float(130):
    print ("a very loud jackhammer")
'''

'''
#Ex41
side1 = input("Enter side 1 length: ")
side2 = input("Enter side 2 length: ")
side3 = input("Enter side 3 length: ")
if float(side1) == float(side2) == float(side3):
    print ("This is an equilateral triangle")
elif float(side1) != float(side2) and float(side1)!= float(side3) and float(side2)!= float(side3):
    print ("This is a scalene triangle")
else:
    print ("This is a isosceles triangle")
'''

'''
#Ex42
#top solution
n = input("Enter note: ")
ln = [x.upper() for x in list(n)]
d = {"C": 261.63,"D": 293.66,"E": 329.63,"F": 349.23,"G": 392.00,"A": 440.00,"B": 493.88}
e = 4-int(ln[1])
print (str(float(d[ln[0]])/2**e) +" Htz")
'''
'''
#Ex43
f = input("Enter frequency: ")
if float(f)-261.63 <= 1 and float(f)-261.63 >=-1:
    print ('C4')
elif float(f)-293.66 <= 1 and float(f)-293.66 >=-1:
    print ('D4')
elif float(f)-329.63 <= 1 and float(f)-329.63 >=-1:
    print ('E4')
elif float(f)-349.23 <= 1 and float(f)-349.23 >=-1:
    print ('F4')
elif float(f)-392.00 <= 1 and float(f)-392.00 >=-1:
    print ('G4')
elif float(f)-440.00 <= 1 and float(f)-440.00 >=-1:
    print ('A4')
elif float(f)-493.88 <= 1 and float(f)-493.88 >=-1:
    print ('B4')
else:
    print ('wrong frequency')
'''

'''
#Ex45
m = input("Enter month (ex: January) : ")
d = input("Enter day (from 1 to 31): ")
#M = m.upper()
if m.upper() == "JANUARY" and float(d) == 1:
    print ("New Year's day")
elif m.upper() == "JULY" and float(d) == 1:
    print ('Canada Day')
elif m.upper() == "DECEMBER" and float(d) == 25:
    print ('Christmas Day')
else:
    print ('No Holiday')
'''

'''
#Ex46
#top solution
l = input("Enter a letter from a to h: ")
n = input("Enter a number from 1 to 8: ")
dl = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,
      "L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,
      "V":22,"W":23,"X":24,"Y":25,"Z":26 }
if int(dl[l.upper()])<=8:
    if int(dl[l.upper()])%2 == 1 and int(n)%2 == 1:
        print ("black")
    elif int(dl[l.upper()])%2 == 0 and int(n)%2 == 0:
        print ("black")
    elif int(dl[l.upper()])%2 == 0 and int(n)%2 == 1:
        print ("white")
    elif int(dl[l.upper()])%2 == 1 and int(n)%2 == 0:
        print ("white")
if int(dl[l.upper()])>8 or int(n)>8:
    print ("not in the chessboard")
'''
'''
#Ex47
month = input("Enter month: ")
day = input("Enter day (dd format, ex 01 as 1st etc..): ")
dm = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,
      "august":8,"september":9,"october":10,"november":11,"december":12}
date = int(str(dm[month.lower()])+str(day))
if 320 <= date < 621:
    print ("Spring")
if 621 <= date < 920:
    print ("Summer")
if 921 <= date < 1220:
    print ("Autumn")
if date >=1220:
    print ("Winter")
if date < 320:
    print ("Winter")
'''

'''
#Ex49
year = input("Enter year: ")
monkey = (list(range(0,2050,12)))
rooster = (list(range(1,2050,12)))
dog = (list(range(2,2050,12)))
pig = (list(range(3,2050,12)))
rat = (list(range(4,2050,12)))
ox = (list(range(5,2050,12)))
tiger = (list(range(6,2050,12)))
hare = (list(range(7,2050,12)))
dragon = (list(range(8,2050,12)))
snake = (list(range(9,2050,12)))
horse = (list(range(10,2050,12)))
sheep = (list(range(11,2050,12)))
if int(year) in rooster:
    print ("rooster")
if int(year) in dog:
    print ("dog")
if int(year) in pig:
    print ("pig")
if int(year) in rat:
    print ("rat")
if int(year) in ox:
    print ("ox")
if int(year) in tiger:
    print ("tiger")
if int(year) in hare:
    print ("hare")
if int(year) in dragon:
    print ("dragon")
if int(year) in snake:
    print ("snake")
if int(year) in horse:
    print ("horse")
if int(year) in sheep:
    print ("sheep")
if int(year) in monkey:
    print ("monkey")
else:
    print ("no record")    
'''

'''
#Ex50
mag = input("Enter magnitude: ")
if 4<=float(mag)<5:
    print("light")
if 5<=float(mag)<6:
    print("moderate")
if 6<=float(mag)<7:
    print("strong")
if 7<=float(mag)<8:
    print("major")
if 8<=float(mag)<9:
    print("great")
if 9<=float(mag)<10:
    print("meteoric")
'''

'''
#Ex51 not completed

a = input("enter a: ")
b = input("enter b: ")
c = input("enter c: ")

root1 = (-b+((b**2-4*a*c)**(1/2)))/2*a
root2 = (-b-((b**2-4*a*c)**(1/2)))/2*a
print (root1)
print (root2)
'''   

'''
#Ex52
m =  input("Enter mark: ")
g = {"A+": 4.3, "A": 4.0, "A-": 3.7, "B+": 3.3 ,"B": 3.0, 
     "B-": 2.7, "C+": 2.3 ,"C": 2, "C-": 1.7, "D+": 1.3, "D":1.0, "F":0}
gk = list(g.keys())
print (g.get(m.upper()))
'''

'''
#Ex53
mag = input("Enter mark: ")
if float(mag)>4.3:
    print("Wrong entry")
if float(mag)==4.3:
    print("A+")
if 4.0<=float(mag)<4.3:
    print("A")
if 3.7<=float(mag)<4.0:
    print("A-")
if 3.3<=float(mag)<3.7:
    print("B+")
if 3.0<=float(mag)<3.3:
    print("B")
if 2.7<=float(mag)<3.0:
    print("B-")
if 2.3<=float(mag)<2.7:
    print("C+")
if 2.0<=float(mag)<2.3:
    print("C")
if 1.7<=float(mag)<2.0:
    print("C-")
if 1.3<=float(mag)<1.7:
    print("D+")
if 1.0<=float(mag)<1.3:
    print("D")
if 0<=float(mag)<1.0:
    print("F")
'''

'''
#Ex54
rating = input("Enter rating: ")
if float(rating)==0.0:
    print("Unacceptable")
elif float(rating)==0.4:
    print("Acceptable")
    print (float(rating)*2500)
elif 0.4<=float(rating)==0.6:
    print("Meritorious")
    print (float(rating)*2500)
else:
    print ("Wrong entry")
'''

'''
#Ex57
calls = input("Enter calls minutes: ")
mex = input("Enter number of messages: ")
if int(calls) <=50 and int(mex)<= 50:
    print ("Your total bill is 16.21$\nSubscription: 15.00$\nAdditional charge (support to 911): 0.44$\n5% taxes: 0.77$")
elif int(calls)>50 and int(mex)<= 50:
    print ("Your total bill is: "+format(15+((int(calls)-50)*0.25) + 0.44 + (15+((int(calls)-50)*0.25) + 0.44)/100*5,'.2f')+" $\nSubscription: 15.00$\nAdditional charge (support to 911): 0.44$\n5% taxes: "+format((15+((int(calls)-50)*0.25) + 0.44)/100*5,'.2f')+" $")
elif int(mex)>50 and int(calls) <=50:
    print ("Your total bill is: "+format(15+((int(mex)-50)*0.15) + 0.44 + (15+((int(mex)-50)*0.15) + 0.44)/100*5,'.2f')+" $\nSubscription: 15.00$\nAdditional charge (support to 911): 0.44$\n5% taxes: "+format((15+((int(mex)-50)*0.15) + 0.44)/100*5, '.2f')+" $")
elif int(mex)>50 and int(calls)>50:
    print ("Your total bill is: "+format(15+((int(calls)-50)*0.25 + (int(mex)-50)*0.15) + 0.44 + (15+((int(calls)-50)*0.25 + (int(mex)-50)*0.15) + 0.44)/100*5,'.2f')+" $\nSubscription: 15.00$\nAdditional charge (support to 911): 0.44$\n5% taxes: "+format((15+((int(calls)-50)*0.25 + (int(mex)-50)*0.15) + 0.44)/100*5,'.2f')+" $")
'''

'''
#Ex58
y = input("Enter year: ")
if int(y)%400 == 0:
    print ("leap year")
elif int(y)%100 == 1:
    print ("leap year")
elif int(y)%4 == 0:
    print ("leap year")
else:
    print ("not leap year")
'''

'''
#Ex 59
y = input ("Enter year: ")
m = input ("Enter month: ")
d = input ("Enter day: ")
lm = (1, 3, 5, 7, 8, 10)
sm = (4, 6, 9, 11)
#long months
if int(m) in lm and int(m) != 12 and int(d)<31:
    print(y, m, int(d)+1)
elif int(m) in lm and int(m) !=12 and int(d)==31:
    print (y,int(m)+1, 1)
#short months
if int(m) in sm and int(m) != 12 and int(d)<30:
    print(y, m, int(d)+1)
elif int(m) in sm and int(m) !=12 and int(d)==30:
    print (y,int(m)+1, 1)
#February only
#if leap
if int(y)%400 == 0 and int(m)==2 and int(d)==29:
    print (y,int(m)+1, 1)
elif int(y)%100 == 1 and int(m)==2 and int(d)==29:
    print (y,int(m)+1, 1)
elif int(y)%4 == 0 and int(m)==2 and int(d)==29:
    print (y,int(m)+1, 1)
if int(y)%400 == 0 and int(m)==2 and int(d)<29:
    print(y, m, int(d)+1)
elif int(y)%100 == 1 and int(m)==2 and int(d)<29:
    print(y, m, int(d)+1)
elif int(y)%4 == 0 and int(m)==2 and int(d)<29:
    print(y, m, int(d)+1)
#if not leap
if int(y)%400 == 1 and int(m)==2 and int(d)==28:
    print (y,int(m)+1, 1)
elif int(y)%100 == 0 and int(m)==2 and int(d)==28:
    print (y,int(m)+1, 1)
elif int(y)%4 == 1 and int(m)==2 and int(d)==28:
    print (y,int(m)+1, 1)
if int(y)%400 == 1 and int(m)==2 and int(d)<28:
    print(y, m, int(d)+1)
elif int(y)%100 == 0 and int(m)==2 and int(d)<28:
    print(y, m, int(d)+1)
elif int(y)%4 == 1 and int(m)==2 and int(d)<28:
    print(y, m, int(d)+1)
#December only    
if int(m) == 12 and int(d)<31:
    print(y, m, int(d)+1)
if int(m) == 12 and int(d)==31:
    print(int(y)+1, 1, 1)
#data entry errors    
if int(m) > 12:
    print("No year has more than 12 months")
if int(m) in sm and int(d)>30:
    print("This month has less than 31 days")
if int(m) ==2 and int(d)>28:
    print("February has only 28 days if the year is not a leap one")    
if int(d) > 31:
    print("No month has mor than 31 days")
'''
'''
#Ex60 not understood but easy
year = input("Enter year: ")
floor = 1
dotw = (int(year)+floor((int(year)-1)/4)-floor((floor-1)/100)+floor((int(year)-1)/400))%7
'''

'''
#Ex61
reg = input("Enter your rego: ")
regl = list(reg)
lc = [i.isnumeric() for i in regl]
if lc.count(False)!=3:
    print ("Wrong Entry")
if lc.count(True)>4:
    print ("Wrong Entry")
if lc.count(True)<3:
    print ("Wrong Entry")    
if lc.count(False) == 3 and lc.count(True) == 3:
    print ("Old rego")
if lc.count(False) == 3 and lc.count(True) == 4:
    print ("New rego")
'''

'''
#Ex62
import random
l = (0,00,1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36,2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
r = (random.choice(l))
reds = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
blacks = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
zeros = (0,00)
print ("The spin resulted in "+str(r))
print ("Pay "+str(r))
if r in reds:
    print ("pay reds")
if r in blacks:
    print ("pay blacks")
if r <19:
    print ("pay 1 to 18")
if r >18:
    print ("pay 19 to 36")
if r == 0:
    print("pay 0")
if r == 00:
    print("pay 00")      
''' 



