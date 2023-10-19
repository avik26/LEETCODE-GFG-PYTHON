class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_string(s: str) -> str:
            result = []
            backspace_count = 0

            for char in reversed(s):
                if char == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    result.append(char)

            return ''.join(result)

        return final_string(s) == final_string(t)
