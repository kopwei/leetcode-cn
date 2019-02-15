#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.26%)
# Total Accepted:    27.1K
# Total Submissions: 64.2K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
class Solution:

    def find_index(self, index_offset, nums, target):
        if not nums:
            return index_offset
        if target <= nums[0]:
            return index_offset
        totalLen = len(nums)
        if target > nums[-1]:
            return index_offset + totalLen
        midPoint = int(totalLen / 2)
        if target <= nums[midPoint - 1]:
            return self.find_index(index_offset, nums[:midPoint], target)
        else:
            return self.find_index(midPoint + index_offset, nums[midPoint:], target)
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.find_index(0, nums, target)

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,4,6,7,8,9], 6))
        
