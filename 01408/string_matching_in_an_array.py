from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        #### [1408. String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/)

        Given an array of string `words`. Return all strings in `words` which is substring of another word in **any** order.

        String `words[i]` is substring of `words[j]`, if can be obtained removing some characters to left and/or right side of `words[j]`.



        **Example 1:**

        ```
        Input: words = ["mass","as","hero","superhero"]
        Output: ["as","hero"]
        Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
        ["hero","as"] is also a valid answer.
        ```

        **Example 2:**

        ```
        Input: words = ["leetcode","et","code"]
        Output: ["et","code"]
        Explanation: "et", "code" are substring of "leetcode".
        ```

        **Example 3:**

        ```
        Input: words = ["blue","green","bu"]
        Output: []
        ```



        **Constraints:**

        - `1 <= words.length <= 100`
        - `1 <= words[i].length <= 30`
        - `words[i]` contains only lowercase English letters.
        - It's **guaranteed** that `words[i]` will be unique.



        Parameters
        ----------
        words: List[str]

        Returns
        -------
        List[str]

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        text = ' '.join(words)
        return [s for s in words if text.count(s) > 1]
