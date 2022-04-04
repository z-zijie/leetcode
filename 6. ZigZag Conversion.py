class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        string_length = len(s)
        group_length = num_rows + num_rows - 2
        if group_length == 0:
            return s
        new_string = ""
        for idx in range(0, string_length, group_length):
            new_string += s[idx]
        for start in range(1, num_rows - 1):
            for idx in range(start, string_length, group_length):
                new_string += s[idx]
                if 0 <= idx - start + group_length - start < len(s):
                    new_string += s[idx - start + group_length - start]
        for idx in range(num_rows - 1, string_length, group_length):
            new_string += s[idx]
        return new_string


if __name__ == "__main__":
    print("6. ZigZag Conversion")
    main = Solution()
    example_string = "A"
    numRows = 1
    print(main.convert(example_string, numRows))
