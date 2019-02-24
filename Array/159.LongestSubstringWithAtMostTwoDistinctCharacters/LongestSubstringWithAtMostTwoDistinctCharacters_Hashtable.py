class Solution(object):
    def longestMostTwoUnique(self, s: 'str') -> int:
        """
        Time - O(n)
        Space - O(1)
        Define the substring as in a sliding window.
        Using a hashtable visited to record the occurence number of each character in the sliding window.
        Using start to record the start of the longest substring(sliding window).
        Using a distinct_count to record the count of different character in the sliding window
        Conditions:
        1. if the char didnot occurs before, distinct_count + 1
        2. the occurence number + 1
        3. if distinct_count > 2 (at most 2 different character), remove the character from the start of the sliding window
        """
        maxlen, start, distinct_count, visited = 0, 0, 0, [0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1

            visited[ord(char)] += 1

            # if distinc_count > 2
            # remove char from start of the sliding window
            while distinct_count > 2:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1

            maxlen = max(maxlen, i - start + 1)
        return maxlen
