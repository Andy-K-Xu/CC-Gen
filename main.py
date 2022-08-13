import random
import string

def main():
    numbers = []
    final_number = ''

    list = ["Visa" , "Mastercard" , "Enroute" , "Discover", "JCB15", "JCB16", "Voyager"]
    company = input("What do you want to generate? \nVisa, Mastercard, Enroute, Discover, JCB15, JCB16, or Voyager?\n")

    while len(numbers) < 3:
            repeat = random.randrange(1000,9999)
            numbers.append(repeat)
            listToString = ' '.join([str(i) for i in numbers])

    def visa():
            beginning = str(random.randrange(4000,4999))
            print(beginning, listToString)
        

    def mastercard():
            beginning = random.randrange(5100,5599)
            print(beginning, listToString)

    def enroute():
            beginning = random.choice([2014, 2149])
            print(beginning, listToString)
        
    def discover():
            beginning = 6011
            print(beginning, listToString)

    def jcb15():
            beginning = random.choice([1800, 2100])
            print(beginning, listToString)

    def jcb16():
            beginning = random.choice([3088, 3096, 3112, 3158, 3337, 3528])
            print(beginning, listToString)
        
    def voyager():
            beginning = 8699
            print(beginning, listToString)
    

    if company == "Visa" in list:
        visa()
    elif company == "Mastercard" in list:
        mastercard()
    elif company == "Enroute" in list:
        enroute()
    elif company == "Discover" in list:
        discover()
    elif company == "JCB15" in list:
        jcb15()
    elif company == "JCB16" in list:
        jcb16()
    elif company == "Voyager" in list:
        voyager()
    else:
        main()
    
main()
