test_cases = [
    (5.6, 4),
    (0.8, -1),
    (1.9, 0),
    (3.4, 5)
]
for starting_number, max_lines in test_cases:
    print(f"Test Case: Starting number={starting_number}, Max lines={max_lines}")
    if max_lines <= 0:
        print("Invalid input. Max lines should be a positive integer.")
    else:
        current_number = starting_number
        for i in range(max_lines):
            for j in range(i + 1):
                print(f"{current_number:.1f}", end=" ")
                current_number += 0.1
            print()
    print()
