import random
import datetime

currentDate = datetime.date.today()

file = open(r"Cards.txt", "w")

def main():
    numbers = []

    list = ["Visa", "Mastercard", "Enroute", "Discover", "JCB15", "JCB16", "Voyager"]
    firstNames = ["Bob", "Greg", "Matt", "Drake", "Odie", "Chip", "Fay", "Tilly", "Amy", "Emily", "Lalia", "Ronat",
                  "Ivria", "Elise", "Bel", "Vereena", "Nana", "Meta", "Thabiti", "Jie", "Rollo", "Cort", "Akanni",
                  "Rothwell", "Emillia", "Pero"]
    lastNames = ["Smith", "Morva", "Svay", "Capellan", "Hunter", "Huttman", "Eheler", "Davidson", "Rook", "Sheen",
                 "Vacio", "Kingswood", "Mcfolley", "Degnan", "Saric", "Wickert", "Merlini", "Delorme", "Xu", "Jr",
                 "Warwick", "Crill", "Wicked", "Lahue", "Swets", "Santos"]
    company = input("What do you want to generate? \nVisa, Mastercard, Enroute, Discover, JCB15, JCB16, or Voyager?\n")

    def fullName():
        nameOne = random.choice(firstNames)
        nameTwo = random.choice(lastNames)
        full = nameOne + " " + nameTwo
        return full

    def randomDate():
        month = str(random.randrange(1, 12))
        randomEXP = random.randrange(3,5) + currentDate.year
        year = str(randomEXP)
        date = month + "/" + year
        return date

    def randomCVV():
        cvv = str(random.randrange(100, 999))
        return cvv

    def lastThree():
        while len(numbers) < 3:
            repeat = random.randrange(1000, 9999)
            numbers.append(repeat)
            listToString = ' '.join([str(i) for i in numbers])
        return listToString

    def visa():
        beginning = str(random.randrange(4000, 4999))
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def mastercard():
        beginning = str(random.randrange(5100, 5599))
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def enroute():
        beginning = str(random.choice([2014, 2149]))
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def discover():
        beginning = str(6011)
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def jcb15():
        beginning = str(random.choice([1800, 2100]))
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def jcb16():
        beginning = str(random.choice([3088, 3096, 3112, 3158, 3337, 3528]))
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def voyager():
        beginning = str(8699)
        end = fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

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


def ask():
    repeat = input("Do you want to generate another card?\nYes or No?\n")
    if repeat == "Yes":
        with open("cards.txt", "w") as output:
            output.write("end")
        main()
        ask()
    else:
        file.close()
        exit()



# ==start==#
main()
ask()
