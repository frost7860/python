total = 0
for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print("Sum of numbers divisible by 3 or 5 below 100:", total)