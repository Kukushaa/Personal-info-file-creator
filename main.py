import os

clear = lambda: os.system('clear')

def file(name, surname):
    try:
        age = int(input("Enter your age please: "))

    except ValueError:
        clear()
        print("Sorry, but enter only nums in age!")
        exit()

    f = open("data.txt", "w+")

    f.write(f"Name: {name}\n"
            f"Surname: {surname}\n"
            f"Age: {age}\n")

    f.close()

file(input("Enter your name please: ").capitalize(),
     input("Enter your surname please: ").capitalize())

clear()

print("File created!")