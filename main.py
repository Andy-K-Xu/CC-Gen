import random
import string
import time
import requests

list = ["Visa" , "Mastercard" , "Amex" , "Discover"]
company = input('enter:\n')
    
def visa():
        beginning = random.randrange(4000,4999)
        repeat = random.randrange(1000,9999)
        print(str(beginning) + " " + str(repeat) + " " + str(repeat) + " " + str(repeat))

if company == "Visa" in list:
    visa()
