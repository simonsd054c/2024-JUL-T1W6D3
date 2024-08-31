# palindrome of a string

# string reversed is also the same as the original string

# simon -> nomis -> equal -> not a palindrome
# anna -> anna -> equal -> palindrome

original_string = input("Enter a string: ")

reversed_string = ""

for character in original_string:
    reversed_string = character + reversed_string

print(reversed_string)

reversed_string_using_another_way = original_string[::-1]

print(reversed_string_using_another_way)

if reversed_string == original_string:
    print("palindrome")
else:
    print("not a palindrome")

if reversed_string_using_another_way == original_string:
    print("palindrome")
else:
    print("not a palindrome")