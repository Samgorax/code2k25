def longestCommonPrefix(strs):
    if not strs:   # agar empty list hai
        return ""
    
    # step 1: assume first string as prefix
    prefix = strs[0]
    
    # step 2: check with other strings
    for s in strs[1:]:
        # reduce prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # prefix ko chhota karo
            if not prefix:
                return ""  # agar prefix empty ho jaye toh done
    
    return prefix


# ---------- testing ----------
print("Test 1:", longestCommonPrefix(["flower", "flow", "flight"]))   # "fl"
print("Test 2:", longestCommonPrefix(["dog", "racecar", "car"]))     # ""
print("Test 3:", longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # "inters"
print("Test 4:", longestCommonPrefix(["a"]))                         # "a"
print("Test 5:", longestCommonPrefix([""]))                          # ""

Output

Test 1: fl
Test 2: 
Test 3: inters
Test 4: a
Test 5: 
