class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in s_to_t_mapping:
                if s_to_t_mapping[s_char] != t_char:
                    return False
            else:
                s_to_t_mapping[s_char] = t_char

            if t_char in t_to_s_mapping:
                if t_to_s_mapping[t_char] != s_char:
                    return False
            else:
                t_to_s_mapping[t_char] = s_char

        return True