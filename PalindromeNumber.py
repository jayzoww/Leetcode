#Palindrome Number: https://leetcode.com/problems/palindrome-number/

#Sol'n 1:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x);
        rev = num[::-1]
            
        if rev == num:
            return True;
        else:
            return False;

#Sol'n 2:
import math;
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False;
        if x == 0:
            return True;
        #Get length of int through log function
        length = int(math.log10(x))+1;
        if length == 1:
            return True;
        rev = 0;
        orig = int(x)
        itr = range(int(length/2))
        #We know how long int is, divide by 2 to get halfway and iterate this many times
        for i in itr:
            #reversed value = original % 10. To append, multiply by 10 and add %10 to end
            rev = rev * 10 + orig % 10;
            #Remove end digits from original
            orig = int(orig / 10);
        #if odd length, divide original by 10 again to remove middle number
        if (length % 2) == 1:
            orig = int(orig / 10);
            
        return orig == rev