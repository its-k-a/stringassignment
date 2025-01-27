# Assignment 1
string = input("Enter some text: ")
string = string.upper()
string = string.replace(" ", "_")
print(f"The modified string is: {string}")
print(f"The length of string is {len(string)}")

#Assignment 2
user_input = input("Enter a string")
processed_string = user_input.replace("", "").lower()
is_palindrome = processed_string == processed_string[::-1]

if is_palindrome:
    print(f'"{user_input}") is a palindrome.')
    print(f'"{user_input}") is not a palindrome')