num = int(input("Enter a number: "))
sum_arm = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_arm += digit ** digits
    temp //= 10

if sum_arm == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")