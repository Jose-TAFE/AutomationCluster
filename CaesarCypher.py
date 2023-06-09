
#Asking to enter a message and key
message = str(input("Please enter your message: ")).upper().replace(" ", "").replace(".", "X")
key = int(input("Enter the key: "))

#Creating a variable to store the cipher message: an open string
cipher_msg = ""

# Shifting the letters according to the cipher key
for l in message:
    if l.isalpha():
        
        #Shifting letters using ascii and wrapping around alphabet characters with modulo and key
        shift_letter= chr((ord(l) - 65 + key) % 26 + 65)
                 
        cipher_msg += shift_letter
            
                   
print(f"The Cyphered message is: {cipher_msg}")
