# 3. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Description
Given a string, find the length of the longest substring without repeating characters.

Example 1:

```
Input: "abcabcbb"
Output: 3
```

Explanation: The answer is "abc", with the length of 3.

Example 2:

```
Input: "bbbbb"
Output: 1
```

Explanation: The answer is "b", with the length of 1.

Example 3:

```
Input: "pwwkew"
Output: 3
```

Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

******
## Solutions
### Brute force - O(n ^ 3, O(n)
* Concept

Check all the substring one by one to see if it has no duplicate character.

### slicing window -
* Algorithm

	* Iterate over all the elements in nums
	* If some number in nums is new to array, append it
	* If some number is already in the array, remove it

### Hash Table - O(n), O(n)
* Algorithm

By using HashSet as a sliding window, checking if a character in the current can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e.[i,j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i,j) to the right by 1 element, then it becomes [i+1,j+1) (left-closed, right-open).

Back to our problem. We use HashSet to store the characters in current window [i,j) (j=i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.

The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.

The reason is that if s[j] have a duplicate in the range [i,j) with index j′, we don't need to increase i little by little. We can skip all the elements in the range [i,j′] and let i to be j′+1 directly.
