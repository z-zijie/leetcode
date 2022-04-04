class Solution:
    bracket_pair = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.bracket_pair:
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if self.bracket_pair.get(top) != char:
                    return False
        return not stack


if __name__ == "__main__":
    print("[LeetCode] [20] [Valid Parentheses]")
    main = Solution()
    s = "()"
    print(main.isValid(s))
    s = "()[]{}"
    print(main.isValid(s))
    s = "(}"
    print(main.isValid(s))
