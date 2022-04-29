words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = []

for w in words:
    m = [w2 for w2 in words if set(w2) == set(w)]
    print(m)
    if m not in anagrams:
        anagrams += [m]

print(anagrams)