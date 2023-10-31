def longest_substring_with_k_distinct_characters(s, k):
  if k <= 0: 
    return ""
  
  max_len = 0
  right = 0
  left = 0 
  char_count= {}
  for right in range(len(s)):
    char = s[right]
    if char not in char_count:
      char_count[char] = 0
    char_count[char]  += 1

    while len(char_count) > k :
      
      char = s[left]
      char_count[char] -= 1
      if char_count[char] == 0:
        del char_count[char]
      left += 1
    



    if right - left +  1 > max_len:
      max_len = max(max_len, right-left + 1)
      max_start = left

  return s[max_start: max_start + max_len]


# Example usage:
s = "eceeba"
k = 2
result = longest_substring_with_k_distinct_characters(s, k)
print(result)  # Output: "ece"
