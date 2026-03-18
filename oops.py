# class Student:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
   
#     sum = 0  
#     for i in self.marks:
#       sum=sum+i
#     print(self.name,sum/len(self.marks))
# s1 = Student("ajit",[20,30,10]) 
   
# class Shrikant:
#   @staticmethod
#   def demo():
#     print("hello")
# s1 = Shrikant()
# s1.demo()
# del s1  
# print(s1)
# class abc:
#  name = "pandharpur"
#  def display(self):
#   print(self.name)
# class xyz(abc):
#   def hello(self):
#     print("jello")
# x = xyz()
# x.display()     
# x.hello()
# class A:
#   color ="red"
# class B(A):
#   wheel = 4
# class C(B):
#   print("ok")
# c1 = C()
# print(c1.color)
# class Person:
#   name ="ajay"
#   @classmethod
#   def changename(m,name):
#     m.name =name
#     print(name)
    
# p1 =Person()
# p1.changename("shrik")
# print(Person.name)
# class Student:
#   def __init__(self,phy,che,math):
#     self.phy=phy
#     self.che=che
#     self.math=math
#   @property
#   def percentage(self):
#       print((self.phy+self.che+self.math)/3)
# s1 = Student(100,90,88)
# s1.percentage
# s1.phy=50
# s1.percentage
# from array import *
# arr =array('i',[10,20,30,40,50])
# for x in arr:
#   print(x)
    
import array as arr 
arr1 =arr.array('i',[10,20,30,40,50])
for x in arr1:
  print(x) 
     
        
  