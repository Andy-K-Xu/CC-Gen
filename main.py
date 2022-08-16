import random

def main():
    numbers = []
    complete = []

    list = ["Visa", "Mastercard", "Enroute", "Discover", "JCB15", "JCB16", "Voyager"]
    firstNames = ["Bob", "Greg", "Matt", "Drake", "Odie", "Chip", "Fay", "Tilly", "Amy", "Emily", "Lalia", "Ronat", "Ivria", "Elise", "Bel", "Vereena", "Nana", "Meta", "Thabiti", "Jie", "Rollo", "Cort", "Akanni", "Rothwell", "Emillia", "Pero"]
    lastNames = ["Smith", "Morva", "Svay", "Capellan", "Hunter", "Huttman", "Eheler", "Davidson", "Rook", "Sheen", "Vacio", "Kingswood", "Mcfolley", "Degnan", "Saric", "Wickert", "Merlini", "Delorme", "Xu", "Jr", "Warwick", "Crill", "Wicked", "Lahue", "Swets", "Santos"]
    company = input("What do you want to generate? \nVisa, Mastercard, Enroute, Discover, JCB15, JCB16, or Voyager?\n")

    def fullName():
        while len(complete) < 2:

    def lastThree():
        while len(numbers) < 3:
            repeat = random.randrange(1000, 9999)
            numbers.append(repeat)
            listToString = ' '.join([str(i) for i in numbers])
        return listToString


    def visa():
        beginning = str(random.randrange(4000, 4999))
        end = beginning + " " + lastThree()
        print(end)

    def mastercard():
        beginning = random.randrange(5100, 5599)
        end = beginning + " " + lastThree()
        print(end)

    def enroute():
        beginning = random.choice([2014, 2149])
        end = beginning + " " + lastThree()
        print(end)

    def discover():
        beginning = 6011
        end = beginning + " " + lastThree()
        print(end)

    def jcb15():
        beginning = random.choice([1800, 2100])
        end = beginning + " " + lastThree()
        print(end)

    def jcb16():
        beginning = random.choice([3088, 3096, 3112, 3158, 3337, 3528])
        end = beginning + " " + lastThree()
        print(end)

    def voyager():
        beginning = 8699
        end = beginning + " " + lastThree()
        print(end)

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
repeat = input("Do you want to generate 100 more?\nYes or No?")

if repeat == "Yes":
    main()
else:
    exit()
