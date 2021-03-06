

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        #### [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

        Given a  string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

        **Example 1:**

        ```
        Input: "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"
        ```

        **Note:** In the string, each word is separated by single space and there will not be any extra space in the string.

        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.reverseWords('Let us take LeetCode contest')
        'teL su ekat edoCteeL tsetnoc'

        Notes
        -----

        References
        ---------

        """
        return ' '.join([w[::-1] for w in s.split(' ')])

