print("Numbers between 1 and 100 divisible by 7 but not by 5:")
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=' ')
print()