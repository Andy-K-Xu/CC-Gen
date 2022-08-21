import random
import datetime
import names

currentDate = datetime.date.today()

file = open(r"Cards.txt", "w")

def main():
    numbers = []

    list = ["Visa", "Mastercard", "Enroute", "Discover", "JCB15", "JCB16", "Voyager"]
    company = input("What do you want to generate? \nVisa, Mastercard, Enroute, Discover, JCB15, JCB16, or Voyager?\n")

    def fullName():
        full = names.get_full_name()
        return full

    def randomDate():
        month = str(random.randrange(1, 12)).zfill(2)
        randomEXP = str(random.randrange(3,5) + currentDate.year)
        date = month + "/" + randomEXP
        return date

    def randomCVV():
        cvv = str(random.randrange(1, 999)).zfill(3)
        return cvv

    def lastThree():
        while len(numbers) < 3:
            repeat = str(random.randrange(1, 9999)).zfill(4)
            numbers.append(repeat)
            listToString = ' '.join([str(i) for i in numbers])
        return listToString

    def visa():
        beginning = str(random.randrange(4000, 4999))
        end = "Visa: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def mastercard():
        beginning = str(random.randrange(5100, 5599))
        end = "Mastercard: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def enroute():
        beginning = str(random.choice([2014, 2149]))
        end = "Enroute: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def discover():
        beginning = str(6011)
        end = "Discover: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def jcb15():
        beginning = str(random.choice([1800, 2100]))
        end = "JCB15: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def jcb16():
        beginning = str(random.choice([3088, 3096, 3112, 3158, 3337, 3528]))
        end = "JCB16: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
        print(end)
        file.write(end + "\n")
        return end

    def voyager():
        beginning = str(8699)
        end = "Voyager: " + fullName() + " | " + beginning + " " + lastThree() + " | " + randomDate() + " | " + randomCVV()
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
    elif repeat == "No":
        file.close()
        exit()
    else:
        ask()



# ==start==#
main()
ask()
