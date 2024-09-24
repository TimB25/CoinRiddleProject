import random
import matplotlib.pyplot as mpl
numberOfFlips = 1000
number_of_tests = 1_000
PRINTCOUNTER = 0
# Statestieken
COUNTUNTILDOUBLEHEADS = []
COUNTUNTILHEADANDTHENCOIN = []


def save_list_of_numbers_to_file(file_name, list_of_numbers):
    bestand = open(file_name,"a")
    for number in list_of_numbers:
        bestand.write(str(number))
        bestand.write(";")
    bestand.close()
def open_list_of_numbers_from_file(file_name):
    bestand = open(file_name, "r")
    gegevens = bestand.read()
    gegevens.split(";")
    bestand.close()
    return gegevens


def countUntilDoubleHeads(list_of_coinflips):
    counter = 0
    last_coin_flipt = 99
    for coin in list_of_coinflips:
        if counter > numberOfFlips:
            raise ValueError("The numer of flips need to be increesed")
        elif(coin == last_coin_flipt and coin == 1):
            return counter - 1
        else:
            last_coin_flipt = coin
            counter +=1

        
def countUntilHeadAndThenCoin(list_of_coinflips):
    counter = 0
    last_coin_flipt = 99
    for coin in list_of_coinflips:
        if (last_coin_flipt == 1 and coin == 0):
            return counter - 1
        else:
            last_coin_flipt = coin
            counter += 1



def generateCoinList(numberOfFlips):
    listOfCoinFlips = []
    while numberOfFlips > 0:
        listOfCoinFlips.append(random.getrandbits(1))
        numberOfFlips -= 1
    return listOfCoinFlips

i = 0
while i < 1000000:

    while number_of_tests > 0:
        number_of_tests -= 1

        coin_list = generateCoinList(numberOfFlips)
        COUNTUNTILDOUBLEHEADS.append(countUntilDoubleHeads(coin_list))
        COUNTUNTILHEADANDTHENCOIN.append(countUntilHeadAndThenCoin(coin_list))




    save_list_of_numbers_to_file("countUntilDoubleHeads.csv", COUNTUNTILDOUBLEHEADS)
    save_list_of_numbers_to_file("countUntilHeadAndThenCoin.csv", COUNTUNTILHEADANDTHENCOIN)
    i +=1









# print(COUNTUNTILDOUBLEHEADS)
# print(COUNTUNTILHEADANDTHENCOIN)

# COUNTUNTILDOUBLEHEADS = sorted(COUNTUNTILDOUBLEHEADS)
# COUNTUNTILHEADANDTHENCOIN = sorted(COUNTUNTILHEADANDTHENCOIN)

# mpl.plot(COUNTUNTILDOUBLEHEADS)
# mpl.plot(COUNTUNTILHEADANDTHENCOIN)
# mpl.show()