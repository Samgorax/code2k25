
def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}
    left = 0
    max_len = 0
    
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            # move left pointer after the last occurrence of ch
            left = last_seen[ch] + 1
        
        # update last seen index of ch
        last_seen[ch] = right
        
        # calculate window length
        max_len = max(max_len, right - left + 1)
    
    return max_len


# -------- testing --------
print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
print(lengthOfLongestSubstring("abcdef"))    # 6 ("abcdef")

Output

3
1
3
6
