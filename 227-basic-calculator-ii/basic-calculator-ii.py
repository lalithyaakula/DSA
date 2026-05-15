class Solution:
    def calculate(self, s: str) -> int:

        arr = []
        num = 0

        # Step 1: Convert string into numbers/operators
        for ch in s:

            if ch == ' ':
                continue

            if ch.isdigit():
                num = num * 10 + int(ch)

            else:
                arr.append(num)
                arr.append(ch)
                num = 0

        arr.append(num)

        # Step 2: Solve * and /
        temp = [arr[0]]

        i = 1

        while i < len(arr):

            op = arr[i]
            val = arr[i + 1]

            if op == '*':
                temp[-1] = temp[-1] * val

            elif op == '/':
                temp[-1] = int(temp[-1] / val)

            else:
                temp.append(op)
                temp.append(val)

            i += 2

        # Step 3: Solve + and -
        ans = temp[0]

        i = 1

        while i < len(temp):

            op = temp[i]
            val = temp[i + 1]

            if op == '+':
                ans += val
            else:
                ans -= val

            i += 2

        return ans