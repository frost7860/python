n = int(input("Enter how many even numbers to print: "))
print("First", n, "even numbers:")
print(*range(2, 2 * n + 1, 2))