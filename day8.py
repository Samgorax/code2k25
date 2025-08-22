def reverseWords(s):
    # step 1: split by spaces
    words = s.strip().split()
    
    # step 2: reverse the list of words
    words.reverse()
    
    # step 3: join back with single space
    return " ".join(words)


# ---------- testing ----------
print("Test 1:", reverseWords("the sky is blue"))        # "blue is sky the"
print("Test 2:", reverseWords("  hello   world  "))      # "world hello"
print("Test 3:", reverseWords("a good   example"))       # "example good a"
print("Test 4:", reverseWords("single"))                 # "single"

Output

Test 1: blue is sky the
Test 2: world hello
Test 3: example good a
Test 4: single
