#Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

#Example:
#Input: ["lint","code","love","you"]
#Output: ["lint","code","love","you"]
#Explanation:
#One possible encode method is: "lint:;code:;love:;you"


class Solution:
    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])

            #update i to end of the str
            i = j + 1 + length
        
        return res
