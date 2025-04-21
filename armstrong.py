def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == number
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
