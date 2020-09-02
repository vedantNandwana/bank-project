import os
#
while True:
    ask = input("Enter What to do..? to add new the details of a person enter {n}\n or to see  details of a person enter {v} \nor to exit enter {q}\n")
    name = 'user'
    number = 0
    person_name = 'none'

    if ask == 'q' or ask == 'Q':
        person_name = input("Enter The Name of that person\n")
        break
    
    readme = open("readme.md" , "w+")
    readme.write("This program is ")

    # Classes and objects
    class Person:
        def __init__(self, name, number):
            self.name = name
            self.number = number

    man = Person(name , number)


    def printit(name , number):
        return print(f"Name = {name} \nNumber = {number}")

    #file managment -v
    def makeFile(userName,prints):

        file = userName + '.txt'
        file1 = open(file , "w+")
        file1.write(prints)
        file1.close()

    def searchFiles(userName):
        try:
            file = userName + '.txt'
            file1 = open(file , "r+")
            print("=======================================")
            print(file1.read())
            print("=======================================")
            file1.write(" *This passbook is given to the client* ")
            file1.close()

        except FileNotFoundError or ValueError:
            print("uff file not found ;(")

    #else if conditionals
    prints = 'none'

    if ask == 'v' or ask == 'V':
        person_name = input("Enter The Name of that person\n")
        searchFiles(person_name)
    
    elif ask == 'n' or ask == 'N':
        person_name = input("Enter The Name \n")
        number = input("Enter The Number \n")
        prints = (f"Name = {person_name} \nNumber = {number}")
        makeFile(person_name,prints)





