# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 23:25:12 2021

@author: paolo
"""

'''
What_is_your_name = 'Paolo'
def name(What_is_your_name):
    
    print ('Hello' +' '+ What_is_your_name)
name(What_is_your_name)'\
'''

'''
height = input("What is the height of the room?")
width = input("What is the width of the room?")
print(str(float(height)*float(width))+" " + "sqm")
'''

'''
#Ex 5
less_than_1litre_bottle = input("How many 0.10$ bottles?")
more_than_1litre_bottle = input("How many 0.25$ bottles?")
print("Your refound is" + " " + str(float(less_than_1litre_bottle)*float(0.10)+float(more_than_1litre_bottle)*float(0.25))+" " + "$")
'''
'''
#Ex 6
meal_cost = input("What is your meal cost?")
tax = format(float(meal_cost)/100*25, '.2f')
tip = format((float(meal_cost)/100*75)/100*18, '.2f')
total = format(float(meal_cost) + float(tip), '.2f')

print("Tax:"+" "+str((tax))+ " " + "$\n"
      "Tip:"+" "+str((tip))+ " " + "$\n"
      "Total:"+" "+str((total))+ " " + "$\n")
'''
'''
#Ex 7
n = int(input("Enter number: "))
print ((n*(n+1))/2)
'''

'''
#Ex 8
n = float(input("Enter balance: "))
n1y = format(float(n + n/100*4), '.2f')
n2y = format(float(n1y) + float(n1y)/100*4, '.2f')
n3y = format(float(n2y) + float(n2y)/100*4, '.2f')
print ("your balance after 1 year:"+" "+str((n1y))+ " " + "$\n"+"your balance after 2 year:"+" "+str((n2y))+ " " + "$\n"+"your balance after 3 year:"+" "+str((n3y))+ " " + "$\n")
'''

'''
#Ex 10
import math
a = input("Enter number a: ")
b = input("Enter number b: ")
sums = str(float(a)+float(b))
diffs = str(float(b)-float(a))
prods = str(float(a)*float(b))
quot = str(float(a)/float(b))
rem = str(float(a)%float(b))
logs = str(math.log(float(a)))
exps = str(float(a)**float(b))
print ("sum:"+" "+sums+"\n"
       "difference:"+" "+diffs+ "\n"
       "product:"+" "+prods+ "\n"
       "quot:"+" "+quot+ "\n"
       "remainder:"+" "+str(rem) + "\n"
       "logarithm:"+" "+logs + "\n"
        "remainder:"+" "+exps + "\n")
'''

'''
#Ex 11
mpg = float(input("Enter MpG: "))
Kml = mpg*1.60934/3.78541
print ("Miles per gallon = "+" " +str(mpg)+"\n" + "km per liter ="+" "+str(Kml))
'''
'''
#Ex 12
import math
t1 = input("Enter lat point 1 in degs: ")
g1 = input("Enter long point 2 in degs : ")
t2 = input("Enter lat point 2 in degs: ")
g2 = input("Enter long point 2 in degs: ")
t1rad = math.radians(float(t1))
g1rad = math.radians(float(g1))
t2rad = math.radians(float(t2))
g2rad = math.radians(float(g2))
distance = 6371.01 * math.acos(math.sin(t1rad) * math.sin(t2rad) + math.cos(t1rad) * math.cos(t2rad) * math.cos(g1rad-g2rad))
print ("The distance is: "+str(distance)+ " Km")
'''
'''
#Ex 12
money = input("Enter $$$: ")
cents = (float(money)*100)
pennies = cents
nickels = cents/5
dime = cents/10
quarters = cents/25
loonie = cents/100
toonie = cents/200
print ("pennies:"+" "+str(pennies)+ " " + "\n"+"nickels:"+" "+str(nickels)+ " " + "\n"+"dime:"+" "+str(dime)+ " " + "\n"+"loonie:"+" "+str(loonie)+ " " + "\n"+"toonie:"+" "+str(toonie))
'''

'''
#Ex 13
height = input("Enter height in feet: ")
height_in_cm = format((float(height)*12)*2.54, '.2f')
print ("Your height in cm: "+str(height_in_cm))
'''
'''
#Ex 34
Loaves = input ("Enter 1 day old loaves n.: ")
Reg_pr = format(float(Loaves)*3.49, '.2f')
disc_lv = float(format((3.49/100)*40, '.2f'))
disc_pr = format(float(Loaves)*disc_lv, '.2f')
print ("Regular price total:"+"     "+str(Reg_pr)+ " " + "\n"+"Discounted price total:"+"  "+str(disc_pr))
'''