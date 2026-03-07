"""
Leet Code: 6
"""


class Solution:
    def convert(self, s: str, num_rows: int) -> str | None:
        # EDGE CASE
        if num_rows == 1 or num_rows >= len(s):
            return s

        # Step : 1 Initialize array of empty string
        rows = [""] * num_rows
        current_row = 0
        going_down = False

        # Step 2: Process each character
        for char in s:
            rows[current_row] += char

            # Check for direction change. We hit top or bottom boundary
            if current_row == 0 or current_row == num_rows - 1:
                going_down = not going_down

            # Move current row based on direction
            if going_down:
                current_row += 1
            else:
                current_row -= 1

        # Step 3: Combine all rows into result
        result = ""
        for each_row in rows:
            result += each_row
        return result


if __name__ == '__main__':
    string = "PAYPALISHIRING"
    row = 3
    print(Solution().convert(s=string, num_rows=row))
