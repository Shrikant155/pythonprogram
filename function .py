# def cal_length(l1):
#   print(len(l1))
# cal_length("ajit")
# a = 10 
# b = 20

# print(f'ajit{type(a)}shrkant{type(b)}') 
# def prod(a,b=2):
#   print(a+b)
# prod(12)      

# def list_len(l1):
#    print(*l1,sep="\n")
  
  
# list1 = [12,2,3,4,5,5] 

# list_len(list1)
# def usdtoinr(usd):
#    inr = usd *92
#    print(f'{usd}usd={inr}inr')
# usdno = int(input("enter usd no"))  
# usdtoinr(usdno)   

# def show(n):
#   if(n==0):
#     return 1
#   print(n)
#   show(n-1)
# show(5)  
  
# def fact(n):
#  if (n==0 or n==1):
#    return 1
#  else:
#    return n*fact(n-1)
# print(fact(5)) 
 
def fact(n):
  sum = 1
  if(n==0 or n==1):
    print("fact=",1)
  else:
    for i in range(1,n+1):
      
      sum=sum*i
    print(sum)       
fact(5)
  