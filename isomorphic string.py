def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping = {}
    for char_s, char_t in zip(s, t):
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapping.values():
                return False
            mapping[char_s] = char_t  
    return True
test_cases = [
    ("egg", "add"),     
    ("foo", "bar"),     
    ("paper", "title"), 
    ("fry", "sky"),     
    ("apples", "apple") 
]
for s, t in test_cases:
    print("Input: s = '{}', t = '{}'".format(s, t))
    print("Output:", is_isomorphic(s, t))
    print()
