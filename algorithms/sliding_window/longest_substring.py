# longest substring with out repeating characters
# "abcabcaa" --> output = 3 (i.e "abc")

def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    max_length = 0
    dict = {}
    while right < len(s):
        if s[right] in dict:
            left += 1
        dict[s[right]] = right
        max_length = max(max_length, right-left + 1)
        right += 1
    return max_length

arr = "abcabcaa"
len =lengthOfLongestSubstring(arr)
print(len)