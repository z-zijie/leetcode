class Solution:
    @staticmethod
    def sgn(x: int) -> int:
        if x > 0:
            return 1
        if x < 0:
            return -1
        return 0

    def reverse(self, x: int) -> int:
        sign = self.sgn(x)
        if sign == 0:
            return 0
        x = sign * x
        stack = []
        while x > 0:
            stack.append(x % 10)
            x = x // 10
        num = stack[0]
        for digit in stack[1:]:
            num = 10 * num + digit
        num = num * sign
        if num > 2 ** 31 - 1 or num < -(2 ** 31):
            return 0
        return num


if __name__ == "__main__":
    print("7. Reverse Integer")
    main = Solution()
    x = 2222
    print(main.reverse(x))