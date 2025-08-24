from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)  # dictionary jisme key=sorted word, value=list of words
    
    for word in strs:
        key = "".join(sorted(word))  # sorted letters ko key banaya
        groups[key].append(word)     # word ko us key ke group me daal diya
    
    return list(groups.values())


# ---------- testing ----------
print("Test 1:", groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print("Test 2:", groupAnagrams([""]))
print("Test 3:", groupAnagrams(["a"]))
print("Test 4:", groupAnagrams(["listen", "silent", "enlist", "google", "gogole"]))

 Output

Test 1: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
Test 2: [['']]
Test 3: [['a']]
Test 4: [['listen', 'silent', 'enlist'], ['google', 'gogole']]
