#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (39.17%)
# Likes:    2892
# Dislikes: 569
# Total Accepted:    462.1K
# Total Submissions: 1.2M
# Testcase Example:  '"/home/"'
#
# Given a string path, which is an absolute path (starting with a slash '/') to
# a file or directory in a Unix-style file system, convert it to the simplified
# canonical path.
# 
# In a Unix-style file system, a period '.' refers to the current directory, a
# double period '..' refers to the directory up a level, and any multiple
# consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
# problem, any other format of periods such as '...' are treated as
# file/directory names.
# 
# The canonical path should have the following format:
# 
# 
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to
# the target file or directory (i.e., no period '.' or double period '..')
# 
# 
# Return the simplified canonical path.
# 
# 
# Example 1:
# 
# 
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
# 
# 
# Example 2:
# 
# 
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
# 
# 
# Example 3:
# 
# 
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stk = []
        for p in path:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if stk: stk.pop()
            else:
                stk.append(p)
        return '/'+'/'.join(stk)


Solution().simplifyPath("/home/")
Solution().simplifyPath("/../")
Solution().simplifyPath("/home//foo/")
# @lc code=end

