class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()

        # Initialize dictionaries to count word occurrences
        word_count = {}

        # Count word occurrences in the first sentence
        for word in words_s1:
            word_count[word] = word_count.get(word, 0) + 1

        # Count word occurrences in the second sentence
        for word in words_s2:
            word_count[word] = word_count.get(word, 0) + 1

        # Find uncommon words that appear exactly once
        uncommon_words = [word for word, count in word_count.items() if count == 1]

        return uncommon_words

        