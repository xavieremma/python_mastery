alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
       shifted_position =  alphabet.index(letter) + shift_amount

       shifted_position %= len(alphabet)
       cipher_text += alphabet[shifted_position]
    print(f"The cyphered text is: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"The cyphered text is: {cipher_text}")

def main():
    print("Welcome to the Caesar Cypher!")
    choice = input("Would you like to Encrypt or Decrypt? ")
    if choice == "Encrypt":
        original_text = input("Please enter the text to be encrypted: ")
        shift_amount = int(input("Please enter the amount of shift you wish to shift to: "))
        encrypt(original_text, shift_amount)

    if choice == "Decrypt":
        original_text = input("Please enter the text to be decrypted: ")
        shift_amount = int(input("Please enter the amount of shift you wish to shift to: "))
        decrypt(original_text, shift_amount)

    choice = input("Would you like to continue? (y/n) ")
    if choice == "y":
        main()
    if choice == "n":
        return
main()



