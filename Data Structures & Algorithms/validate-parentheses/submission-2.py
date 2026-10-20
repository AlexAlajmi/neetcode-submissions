class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"{":"}", "[":"]", "(":")"}
        stack = []

        for i in s:
            if i in valid:
                # i is an opener: remember it
                stack.append(i)
            else:
                # i is a closer

                # 1. nothing to match it with?
                if stack == []:
                    return False

                # 2. take the most recent opener off and save it
                top = stack.pop()

                # 3. does that opener's closer match i?
                if valid[top] != i:
                    return False

        # made it through the whole string: valid only if nothing is left open
        return stack == []