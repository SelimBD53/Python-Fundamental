# class Solution:
#     def two_sum(nums,target):
#         seen = {}
#         for i in range(len(nums)):
#             second_num = target - nums[i]
#             if second_num in seen:
#                 return [i,seen[second_num]]
#             seen[nums[i]] = i