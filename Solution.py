class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == None or type(s) != str or len(s) == 0):
            return 0

        maxLength = 0
        p1 = p2 = 0 
        charactersAppearance = dict()

        for x in s:
          previousPosition = charactersAppearance.get(x)      

          if (previousPosition != None and previousPosition >= p1):
            p1 = previousPosition + 1
          
          charactersAppearance[x] = p2

          length = p2 - p1 + 1
          maxLength = max(length, maxLength)

          p2 += 1

        return maxLength

print(Solution().lengthOfLongestSubstring("abba"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring('abrkaabcabcdefghijjxxx'))