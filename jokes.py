import pyjokes
#print 10 jokes 
for i in range(0,1000000):
  joke = pyjokes.get_joke()
  print(i," = ",joke)
