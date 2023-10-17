class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words
        words = s.split()
        # Reverse each word and store in a list
        reversed_words = [word[::-1] for word in words]
        # Join the reversed words with spaces to form the final sentence
        return ' '.join(reversed_words)

        