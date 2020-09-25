from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Given an array of strings `products` and a string `searchWord`. We want to design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

        Return *list of lists* of the suggested `products` after each character of `searchWord` is typed.


        **Example 1:**

        ```
        Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
        Output: [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
        ]
        Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
        After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
        After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
        ```

        **Example 2:**

        ```
        Input: products = ["havana"], searchWord = "havana"
        Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        ```

        **Example 3:**

        ```
        Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
        Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
        ```

        **Example 4:**

        ```
        Input: products = ["havana"], searchWord = "tatiana"
        Output: [[],[],[],[],[],[],[]]
        ```



        **Constraints:**

        - `1 <= products.length <= 1000`
        - There are no repeated elements in `products`.
        - `1 <= Σ products[i].length <= 2 * 10^4`
        - All characters of `products[i]` are lower-case English letters.
        - `1 <= searchWord.length <= 1000`
        - All characters of `searchWord` are lower-case English letters.


        Parameters
        ----------
        products: List[str]
        searchWord: str

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        from bisect import bisect_left
        i, res, prefix = 0, [], ''
        products.sort()
        for ch in searchWord:
            prefix = prefix + ch
            i = bisect_left(products, prefix, i)
            res.append([w for w in products[i:i+3] if w.startswith(prefix)])
        return res

    def suggestedProducts01(self, products: List[str], searchWord: str) -> List[List[str]]:
        from collections import defaultdict

        class Trie:
            def __init__(self):
                self.sub = defaultdict(Trie)
                self.suggestions = []

            def add_suggestions(self, word):
                if len(self.suggestions) < 3:
                    self.suggestions.append(word)

        products = sorted(products)
        root = Trie()
        for word in products:
            node = root
            for ch in word:
                node = node.sub[ch]
                node.add_suggestions(word)

        res, node = [], root
        for ch in searchWord:
            node = node.sub[ch]
            res.append(node.suggestions)

        return res



