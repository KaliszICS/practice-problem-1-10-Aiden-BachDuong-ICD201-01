'''
    Lesson: Math Library Practice
    Author: Aiden Bach Duong
    Date Created: October 2, 2024
    Date Last Modified: October 2, 2024
'''
import math 

def q1(): 
  #Write Assignment code here
  num = input("Input a number: ")
  num = float(num)
  print(math.sqrt(num))

def q2(): 
  #Write Assignment code here
  num1 = input("Input a number: ")
  num1 = int(num1)
  print(math.isqrt(num1))

def q3(): 
  #Write Assignment code here
  num2 = input("Input a number: ")
  num2 = float(num2)
  print(math.floor(num2))

def q4(): 
  #Write Assignment code here
  num3 = input("Input a number: ")
  num3 = float(num3)
  print(math.ceil(num3))

def q5(): 
  #Write Assignment code here
  num4 = input("Input a number: ")
  num5 = input("Input another number: ")
  num4 = float(num4)
  num5 = float(num5)
  print(math.floor((num4*num5)/2))



#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
q4()
q5()
'''