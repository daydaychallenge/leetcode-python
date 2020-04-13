

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        #### [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion)

        The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:  (you may want to display this pattern in a fixed font for better  legibility)

        ```
        P   A   H   N
        A P L S I I G
        Y   I   R
        ```

        And then read line by line: `"PAHNAPLSIIGYIR"`

        Write the code that will take a string and make this conversion given a number of rows:

        ```
        string convert(string s, int numRows);
        ```

        **Example 1:**

        ```
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        ```

        **Example 2:**

        ```
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:

        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        ```

        Parameters
        ----------
        s: str
        numRows: int

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.convert('PAYPALISHIRING', 3)
        'PAHNAPLSIIGYIR'
        >>> sol.convert('PAYPALISHIRING', 4)
        'PINALSIGYAHRPI'

        Notes
        -----

        References
        ---------

        """
        if numRows <= 1 or numRows >= len(s):
            return s
        rows = ['' for _ in range(numRows)]
        index, step = 0, 1
        for c in s:
            rows[index] += c
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(rows)
