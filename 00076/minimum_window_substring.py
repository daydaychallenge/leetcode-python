
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        #### [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

        Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

        **Example:**

        ```
        Input: S = "ADOBECODEBANC", T = "ABC"
        Output: "BANC"
        ```

        **Note:**

        - If there is no such window in S that covers all characters in T, return the empty string `""`.
        - If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

        Parameters
        ----------
        s: str
        t: str

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        from collections import Counter
        pattern = Counter(t)
        slow = formed = 0
        res = ''
        for fast, c in enumerate(s):
            if c not in pattern:
                continue
            pattern[c] -= 1
            if pattern[c] == 0:
                formed +=1
            while formed == len(pattern) and slow <= fast:
                if not res or len(res) > fast-slow+1:
                    res = s[slow:fast+1]
                ch = s[slow]
                if ch in pattern:
                    pattern[ch] += 1
                if pattern[ch] == 1:
                    formed -= 1
                slow += 1
        return res

