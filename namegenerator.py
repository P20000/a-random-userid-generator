import csv
from random import choice
from mixingalgorithm import merge_strings
from random import randint
from random import choice
def random_masala():
    list1 = ['123456789', "!@#$%^&*()", "1@3$5^7*9"]
    return merge_strings(choice(list1), choice(list1))


def namegenerator_():
    finalnames = []
    with open("names.csv", 'r') as file1:
        read = csv.reader(file1)
        header = next(file1)
        row = [row for row in read]
        names = [ro[1] for ro in row]
        finalnames.append(names)
        file1.close()

    with open("most-common-name~2Fsurnames.csv", 'r') as file2:
        read = csv.reader(file2)
        header = next(file2)
        row = [row for row in read]
        surnames = [ro[1] for ro in row]
        finalnames.append(surnames)
        file2.close()
    choice(finalnames[0])
    thename = [choice(finalnames[0]), choice(finalnames[0]), choice(finalnames[1]).capitalize()] 
    return thename[0], thename[0], thename[1]
    


if __name__ == "__main__":
    k = namegenerator_()
    username = merge_strings(k[0], k[2])
    passwrd= merge_strings(username, random_masala())
    print(k)
    
    print(f"username = {username}\n password = {passwrd[0:20]}")
