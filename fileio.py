# total = 0
# def sum(arg1,arg2):
#   total =arg1 +arg2
#   print(total)
# sum(10,20)
# print(total)  
# def pack_example(*args):
#   print(args)
# pack_example(1,2,3,'a','b')
  
# def unpack_example(a,b,c):
#   print(a,b,c)
# val = [1,2,3]
# unpack_example(*val) 
# with open("demo.txt","r") as file:
#   lines =file.readlines()
#   for line in lines:
#     print(line)
# file.close() 
# 
with open("demo.txt","w") as f:
  f.write("hello")
with open("demo.txt") as f:
   data =f.read()
   word="hello"
   if(word in data):
       print("found")  
   else:
     print("not found") 

