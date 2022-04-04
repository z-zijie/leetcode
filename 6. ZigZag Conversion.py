class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string_length = len(s)
        group_length = numRows + numRows - 2
        if group_length == 0:
            return s
        group_count = string_length // group_length
        remainder = string_length - group_count * group_length
        new_string = ""
        for idx in range(0, string_length, group_length):
            new_string += s[idx]
        for start in range(1, numRows - 1):
            for idx in range(start, string_length, group_length):
                new_string += s[idx]
                if 0 <= idx - start + group_length - start < len(s):
                    new_string += s[idx - start + group_length - start]
        for idx in range(numRows - 1, string_length, group_length):
            new_string += s[idx]
        return new_string


if __name__ == "__main__":
    print("6. ZigZag Conversion")
    main = Solution()
    s = "A"
    numRows = 1
    print(main.convert(s, numRows))
