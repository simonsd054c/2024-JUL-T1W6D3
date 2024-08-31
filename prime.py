# if a number is prime
# prime number is a number that is divisible by 1 and itself only
# 16 -> 1, 2, 4, 8, 16 -> not a prime number
# 17 -> 1, 17 -> a prime number

number = int(input("Enter a number: ")) # 16

for i in range(2, number):
    if number % i == 0:
        print("Not a prime")
        break
else:
    print("A prime")