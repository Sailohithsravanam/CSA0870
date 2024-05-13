def is_perfect(num):
    factors_sum = sum(i for i in range(1, num) if num % i == 0)
    return factors_sum == num
N = int(input("Enter the number of perfect numbers you want: "))
M = int(input("Enter the number of factors you want to display for each perfect number: "))
count = 0
number = 1
while count < N:
    if is_perfect(number):
        factors = [i for i in range(1, number + 1) if number % i == 0][:M]
        factors_str = ', '.join([str(factor) for factor in factors])
        print(f"First {M} factors of {number} are: {factors_str}")
        count += 1
    number += 1
