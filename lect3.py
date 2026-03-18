# #list decalred
# list = [1,2,3,4,5,6]
# print(list)
# print("item in index 5=",list[5])
# #this is append method add  ele to end 
# list.append(10)
# print(list)
# list2 = []
# #list reveresed order result in original list present mutable list
# list.reverse()
# print(list)
# #
# print(len(list))
# tup = (3,2,3,4,5,5,)

# print(tup.count(5))
# for i in range (1,25):
#   if  i ==11:
#     break
# #   print(i)
# list1 = [1,2,1]
# list2 = []
# list2 = list1.copy()
# list2.reverse()
# if list1 == list2:
#   print("palindrome")
# else:
#   print("not planidrome")  
tup1 = ("A","B","A")
count_a = tup1.count("A")
print(count_a)
list = []
for i in tup1:
  if i == "A":
    list.append(i)
print(list)    
