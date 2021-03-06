

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        #### [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

        Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'`.

        ```
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        ```

        The matching should cover the **entire** input string (not partial).

        **Note:**

        - `s` could be empty and contains only lowercase letters `a-z`.
        - `p` could be empty and contains only lowercase letters `a-z`, and characters like `.` or `*`.

        **Example 1:**

        ```
        Input:
        s = "aa"
        p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
        ```

        **Example 2:**

        ```
        Input:
        s = "aa"
        p = "a*"
        Output: true
        Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
        ```

        **Example 3:**

        ```
        Input:
        s = "ab"
        p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".
        ```

        **Example 4:**

        ```
        Input:
        s = "aab"
        p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
        ```

        **Example 5:**

        ```
        Input:
        s = "mississippi"
        p = "mis*is*p*."
        Output: false
        ```

        Parameters
        ----------
        s: str
        p: str

        Returns
        -------
        bool

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatchV01(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = True

        for j in range(2, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] in {s[i-1], '.'}:
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]

        return dp[-1][-1]


