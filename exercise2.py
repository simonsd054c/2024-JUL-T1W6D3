# factorial
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# 12! = 12 * 11 * 10 * ... * 2 * 1 = ???

num = int(input("Enter a number: "))
fact = 1

# for i in range(1, num + 1):
#     fact *= i
#     # fact = fact * i

for i in range(num, 0, -1):
    fact *= i

print(fact)