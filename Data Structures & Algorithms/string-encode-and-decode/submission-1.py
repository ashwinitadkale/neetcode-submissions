from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):

            j = i

            # move j until #
            while s[j] != "#":
                j += 1

            # get length
            length = int(s[i:j])

            # extract word
            word = s[j+1 : j+1+length]

            res.append(word)

            # move i to next encoded word
            i = j + 1 + length

        return res