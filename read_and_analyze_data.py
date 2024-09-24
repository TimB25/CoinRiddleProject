









def save_list_of_numbers_to_file(file_name, list_of_numbers):
    bestand = open(file_name,"a")
    for number in list_of_numbers:
        bestand.write(str(number))
        bestand.write(",")
    bestand.close()
def open_list_of_numbers_from_file(file_name):
    bestand = open(file_name, "r")
    gegevens = bestand.read()
    gegevens.split(",")
    bestand.close()
    return gegevens




data = open_list_of_numbers_from_file("countUntilDoubleHeads.csv")