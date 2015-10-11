"""
Author: spyros lalos <spyroslal@gmail.com>

-Time complexity: O(n)
-Space complexity: O(n)

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.
"""

class Solution( object ):
    """
        :type pattern: str
        :type str: str
        :rtype: bool
    """
    def wordPattern( self, pattern, str  ):
        list1, dict, list2 = str.split(" "), {}, []
        if len( list1 ) != len( pattern ):
            return False

        for i in xrange( len( pattern ) ):
            if pattern[i] not in dict:
                if list1[i] in dict.values():
                    return False
                dict[pattern[i]]=list1[i]
                list2.append( list1[i] )
            else:
                list2.append( dict[pattern[i]] )

        return list1 == list2

