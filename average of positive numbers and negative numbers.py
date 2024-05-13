positive_numbers = []
negative_numbers = []

def calculate_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0
numbers = [-1, 43, -87, -29, 1, -9]
for num in numbers:
    if num == -1:
        break
    elif num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)
average_positive = calculate_average(positive_numbers)
average_negative = calculate_average(negative_numbers)
print(f"The average of negative numbers is: {average_negative:.8f}")
print(f"The average of positive numbers is: {average_positive:.8f}")
