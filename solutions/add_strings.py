from time import time
from typing import List

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        ord0 = ord('0')

        while i>=0 or j>=0:
            digit_i = ord(num1[i]) - ord0 if i>=0 else 0
            digit_j = ord(num2[j]) - ord0 if j>=0 else 0

            this_sum = digit_i + digit_j + carry
            carry = this_sum // 10
            res += str(this_sum % 10)
            i -= 1
            j -= 1
        if carry:
            res += str(carry)
        return res[::-1]


if __name__ == "__main__":
    start_time = time()
    S = Solution()
    num1 = "456"; num2 = "77"
    print(S.addStrings(num1,num2))
    print(time() - start_time,"ms")
