import pyttsx3
import pyjokes
from faker import Faker
joke = pyjokes.get_joke()
print("joke =",joke)
fake =Faker()
print("adhar=",fake.name())
print("adhar=",fake.date_of_birth(minimum_age=10,maximum_age=80))
engine =pyttsx3.init()
engine.say("hello all in one plg")
engine.runAndWait()
import random
numbers =random.randrange(101,10001)
print(numbers)