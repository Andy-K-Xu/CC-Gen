import random
import string
import time
import requests

list = ["Visa" , "Mastercard" , "Amex" , "Discover"]
company = input('enter:\n')
numbers = []

    
while len(numbers) < 4:
        repeat = random.randrange(4000,4999)
        numbers.append(repeat)
        
def visa():
        beginning = random.randrange(4000,4999)
        listToString = ' '.join([str(i) for i in numbers])
        print(listToString)

        
if company == "Visa" in list:
    visa()
