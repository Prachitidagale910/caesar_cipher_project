alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#combinging encrypt and decrypt
def ceaser(start_text, shift_amt, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet_list.index(letter)
        

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet_list.index(letter)
        new_position = (position + shift_amount) % len(alphabet_list)
        new_letter = alphabet_list[new_position]
        cipher_text += new_letter
    
    print("The encoded text is : ", cipher_text)
    
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet_list.index(letter)
        new_position =  (position - shift_amount) % len(alphabet_list)
        plain_text += alphabet_list[new_position]
    print(f"the decoed text is {plain_text}")

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

encrypt(text, shift)