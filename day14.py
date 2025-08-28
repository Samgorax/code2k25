#sql
substrings with exactly K distinct 
   = substrings with at most K distinct 
     - substrings with at most (K-1) distinct


from collections import defaultdict

def countSubstringsWithAtMostK(s: str, k: int) -> int:
    n = len(s)
    count = 0
    left = 0
    freq = defaultdict(int)
    distinct = 0
    
    for right in range(n):
        # include right char
        if freq[s[right]] == 0:
            distinct += 1
        freq[s[right]] += 1
        
        # shrink window if distinct > k
        while distinct > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                distinct -= 1
            left += 1
        
        # all substrings ending at right with at most k distinct
        count += (right - left + 1)
    
    return count


def countSubstringsWithExactlyK(s: str, k: int) -> int:
    return countSubstringsWithAtMostK(s, k) - countSubstringsWithAtMostK(s, k - 1)


# -------- testing --------
print(countSubstringsWithExactlyK("pqpqs", 2))  # 7
print(countSubstringsWithExactlyK("abcba", 2))  # 7
print(countSubstringsWithExactlyK("a", 1))      # 1

 
Output

7
7
1
