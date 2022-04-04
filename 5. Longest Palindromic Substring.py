class Solution:
    @staticmethod
    def find_palindromic_substr(pos: int, s: str):
        length = 1
        while pos - length >= 0 and pos + length < len(s) and s[pos - length] == s[pos + length]:
            length += 1
        length = length - 1
        substr = s[pos - length:pos + length + 1].replace('#', '')
        return substr

    def longestPalindrome(self, s: str) -> str:
        longest_substr = ''
        s = '#'.join(s)
        for center, _ in enumerate(s):
            substr = self.find_palindromic_substr(center, s)
            if len(substr) > len(longest_substr):
                longest_substr = substr
        return longest_substr


if __name__ == "__main__":
    print("5. Longest Palindromic Substring")
    main = Solution()
    example_string = "abcdcbsas"
    print(main.longestPalindrome(example_string))
