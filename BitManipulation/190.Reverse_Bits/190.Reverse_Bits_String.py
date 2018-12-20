class Solution(object):
    def reverseBitsString(self, n):
        """
        Time - O(length(n)) = O(32)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        string = bin(n)
        if "-" in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)

    def reverseBitsString2(self, n):
        """
        Time - O(length(n)) = O(32)
        Space - O(1)
        :type n: integer
        :rtype: integer
        """
        # originBin ='{0:032b}'.format(n)
        # reverseBin = originBin[::-1]
        # return int(reverseBin, 2)
        return int('{0:032b}'.format(n)[::-1], 2)
