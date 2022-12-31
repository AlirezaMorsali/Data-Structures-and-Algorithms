"""3. Longest Substring Without Repeating Characters
Medium
30.9K
1.3K
Companies

Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""


def lenght_of_longest_substring(s: str):
    max_len = 0
    current_sub = ""
    for i, c in enumerate(s):
        if c in current_sub:
            if (new_len := len(current_sub)) > max_len:
                max_len = new_len
            ind = current_sub.find(c)
            current_sub = current_sub[ind+1:]
        current_sub += c
    if (new_len := len(current_sub)) > max_len:
        max_len = new_len

    return max_len


# Output: 3
print(lenght_of_longest_substring(s="abcabcbb"))
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
print(lenght_of_longest_substring(s="bbbbb"))
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

print(lenght_of_longest_substring(s="pwwkew"))
# Input: s = "pwwkew"

print(lenght_of_longest_substring(s="ab"))
