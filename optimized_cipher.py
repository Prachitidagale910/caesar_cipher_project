alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amt, cipher_direction):
    result_text = ""
    
    # Adjust shift_amt based on the direction (positive for encrypt, negative for decrypt)
    if cipher_direction == 'decode':
        shift_amt = -shift_amt
    
    for letter in start_text:
        if letter in alphabet_list:  # Only shift alphabet characters
            position = alphabet_list.index(letter)
            new_position = (position + shift_amt) % len(alphabet_list)  # Handle wrap-around
            result_text += alphabet_list[new_position]
        else:
            result_text += letter  # Non-alphabet characters remain unchanged
    

    print(f"The {cipher_direction}d text is: {result_text}")

# Example usage:
direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
message = input("Enter your message: ").lower()
shift = int(input("Enter the shift amount: "))

caesar(message, shift, direction)
