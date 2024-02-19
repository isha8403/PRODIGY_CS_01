alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Enter Your Text :")
#Shift value
shift= int(input("Enter the Shift Value :"))

def encrypt(message):
    cipher = ""
    for char in message:
        if char.isalpha():
            index = alphabet.index(char.lower())
            cipher += alphabet[(index + shift) % 26]
        else:
            cipher += char
    return cipher
def decrypt(cipher):
    plain = ""
    for char in cipher:
        if char.isalpha():
            index = alphabet.index(char.lower())
            plain += alphabet[(index - shift) % 26]
        else:
            plain += char
    return plain

cipher = encrypt(message)
print("Encryted Text :" , cipher)
plain = decrypt(cipher)
print("Decrypted Text :", plain)
            
