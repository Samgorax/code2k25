def permute(s):
    result = []
    chars = sorted(list(s))  # sorting so duplicates handle easily
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            result.append("".join(path))
            return
        
        for i in range(len(chars)):
            # skip already used chars
            if used[i]:
                continue
            
            # skip duplicates (important condition!)
            if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                continue
            
            # choose
            used[i] = True
            path.append(chars[i])
            
            # explore
            backtrack(path)
            
            # undo
            path.pop()
            used[i] = False

    backtrack([])
    return result


# ---------- testing ----------
print("Test 1:", permute("abc"))
print("Test 2:", permute("aab"))
print("Test 3:", permute("ab"))
print("Test 4:", permute("a")) 

Output

Test 1: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
Test 2: ['aab', 'aba', 'baa']
Test 3: ['ab', 'ba']
Test 4: ['a']
