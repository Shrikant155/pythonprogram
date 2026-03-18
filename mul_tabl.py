# num =int(input("enter no"))
# for i in range (1,11):
#  print(f'{num} X {i} = {num*i}')
# n = int(input("no"))
# i = 0
# sum = 0
# while(i<n):
#   sum+=i
#   i+=1
# print(sum)  
# no = int(input("no"))
# sum = 0

# for i in range (1,no):
#   sum+=i
# print(sum)  
 
def add(a,b,c):
  return a+b+c
nums =[1,2,3]
print(add(*nums))
def info(**data):
  for k,v in data.items():
    print(f'{k}={v}')
info(name="shrikant",age=30)    
def greet(*names):
  for i in names:
    print(i)
greet("ajay","rohan","sitaram")    
def greet1(name="world"):
  print(f'hello{name}')
greet1()
greet1("ajay")  