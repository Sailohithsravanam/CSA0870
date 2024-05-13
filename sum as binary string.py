def add_binary(a, b):
    carry = 0
    result = ""
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry:
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        carry = sum // 2
        result = str(sum % 2) + result
    
    return result
test_cases = [
    ("11", "1"),
    ("1010", "1011"),
    ("1111", "1010"),
    ("101101", "1100"),
    ("1011", "1111")
]
for a, b in test_cases:
    print(f"Input: a = \"{a}\", b = \"{b}\"")
    print("Output:", add_binary(a, b))
    print()
