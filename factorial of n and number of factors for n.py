def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
test_cases = [0, -5, 1, 20, "3A"]
for N in test_cases:
    print(f"Test Case: N={N}")
    try:
        n = int(N)
        if n <= 0:
            print("Invalid input. N should be a positive integer.")
        else:
            fact = 1 if n == 0 else factorial(n)
            factor_count = count_factors(n)
            print(f"{n} Factorial: {fact}")
            print(f"Number of factors for {n}: {factor_count}")
    except ValueError:
        print("Invalid input. N should be an integer.")
    print()
