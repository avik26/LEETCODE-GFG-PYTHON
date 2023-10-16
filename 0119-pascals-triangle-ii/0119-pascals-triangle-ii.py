from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
        # Initialize the first row with 1.
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Calculate each element in the current row.
            new_row = [1]
            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])
            new_row.append(1)
            
            row = new_row  # Update the current row with the new row.
        
        return row
