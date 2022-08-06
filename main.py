import random
import string
import time
import requests

list = ["Visa" , "Mastercard" , "Amex" , "Discover"]
visa_list = [4539, 4556, 4916, 4532, 4929, 4024, 4485, 4716, 4207, 4266]

company = input('enter:\n')
    
def visa():
        beginning = random.choice(visa_list)
        complete = beginning + random.randrange(0001,9999)
        print(complete)

if company == "Visa" in list:
    visa()
