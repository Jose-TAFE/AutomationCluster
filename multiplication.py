#Welcome message
print("Welcome to multiplication table")

#Request to enter a name
username = input("\nPlease enter your name:")

#Request to choose a number to multiply
choicenumber = int(input(f"{username} please enter the number you wish to multiply: "))

#Confirmation of number
print(f"you entered the number: {choicenumber}: ")
confirmation = str(input("Press Y to continue or N to enter another number: ")).lower()
if confirmation == "y":

#Loop the number multiplied from 1 to 12
    for i in range(1,13):
        print(f"{choicenumber} x {i} = {choicenumber*i}")
else:
    print ("\nEnter another number: ")
    choicenumber = int(input("Correct number:"))
    for i in range(1,13):
        print(f"{choicenumber} x {i} = {choicenumber*i}")

#Thank you message
print ("\nThanks for multiplying")    