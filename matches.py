def matches(s1, s2):
    count = 0
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] == s2[i]:
            count += 1
    return count
test_cases = [
    ("what", "watch"),
    (" ran", "van"),
    (" rain", " turn"),
    (" python", "py"),
    ("man", "women")
]
for s1, s2 in test_cases:
    print(f"Input: s1 = \"{s1}\", s2 = \"{s2}\"")
    print("Output:", matches(s1, s2))
    print()
