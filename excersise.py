
def greet():
    print("Hello 1")
    print("Hello 2")
    print("Hello 3")


greet()



def count_vowels(input_string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    input_string = input_string.lower()  # Convert the string to lowercase
    count = 0  # Initialize the count
    
    # Iterate through the string and count the vowels
    for char in input_string:
        if char in vowel_list:
            count += 1
    
    return count  # Return the total count of vowels


# Get user input
user_input = input("Please enter a string: ")

# Call the function and print the result
vowel_count = count_vowels(user_input)
print(f"Total vowels in the string: {vowel_count}")
