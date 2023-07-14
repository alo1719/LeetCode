#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (51.58%)
# Likes:    3632
# Dislikes: 923
# Total Accepted:    538.1K
# Total Submissions: 1M
# Testcase Example:  '00000010100101000001111010011100'
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
#
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 2 above, the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.
#
#
#
# Example 1:
#
#
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100
# represents the unsigned integer 43261596, so return 964176192 which its
# binary representation is 00111001011110000010100101000000.
#
#
# Example 2:
#
#
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101
# represents the unsigned integer 4294967293, so return 3221225471 which its
# binary representation is 10111111111111111111111111111111.
#
#
#
# Constraints:
#
#
# The input must be a binary string of length 32
#
#
#
# Follow up: If this function is called many times, how would you optimize it?
#
#

# @lc code=start
# TC: O(1)  SC: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        mask1 = 0b01010101010101010101010101010101
        mask2 = 0b00110011001100110011001100110011
        mask4 = 0b00001111000011110000111100001111
        mask8 = 0b00000000111111110000000011111111
        mask16 = 0b00000000000000001111111111111111
        # flip 2 bits
        n = n>>1&mask1|(n&mask1)<<1
        # flip 4 bits
        n = n>>2&mask2|(n&mask2)<<2
        # flip 8 bits
        n = n>>4&mask4|(n&mask4)<<4
        # flip 16 bits
        n = n>>8&mask8|(n&mask8)<<8
        # flip 32 bits
        n = n>>16&mask16|(n&mask16)<<16
        return n
# @lc code=end
