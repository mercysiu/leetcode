class Solution(object):
    def search(self, nums, target):
        first, last = 0, len(nums) -1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                first = mid + 1
            if nums[mid] > target:
                last = mid - 1
        return -1