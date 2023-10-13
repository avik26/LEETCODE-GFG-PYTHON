class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}  # Dictionary to store the index of strings in list1
        min_index_sum = float('inf')  # Initialize the minimum index sum
        common_strings = []  # List to store common strings with the minimum index sum

        # Create a dictionary to map strings to their indices in list1
        for i, string in enumerate(list1):
            index_map[string] = i

        # Iterate through list2 and find common strings
        for j, string in enumerate(list2):
            if string in index_map:
                # Calculate the index sum for the common string
                index_sum = j + index_map[string]

                # If the index sum is less than the minimum, update the minimum
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    common_strings = [string]
                # If the index sum is equal to the minimum, append the string
                elif index_sum == min_index_sum:
                    common_strings.append(string)

        return common_strings
