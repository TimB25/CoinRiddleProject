import pandas as pd
import csv




###Inputs###
FILENAME_INPUT = "countUntilHeadAndThenCoin.csv"
FILENAME_OUTPUT = "compressedCountUntilHeadAndThenCoin.csv"
###Inputs###

VALUES = {}







def save_dictionary_of_numbers_to_file(file_name, dictionary):
    with open(file_name, "w") as f:
        w = csv.writer(f, delimiter = ";")
        w.writerows(dictionary.items())

def open_list_of_numbers_from_file(file_name):
    bestand = open(file_name, "r")
    gegevens = bestand.read()
    gegevens = gegevens.split(";")
    bestand.close()
    
    return gegevens


data = open_list_of_numbers_from_file(FILENAME_INPUT)
for value in data:
    if (value in VALUES.keys()):
        VALUES[value] += 1
    else:
        VALUES[value] = 1

save_dictionary_of_numbers_to_file(FILENAME_OUTPUT, VALUES)
