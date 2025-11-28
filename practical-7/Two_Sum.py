<<<<<<< HEAD
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return [] 
nums=[1,2,3,45,5,6]
target=9
print(twoSum(nums,target))
=======
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return [] 
nums=[1,2,3,45,5,6]
target=9
print(twoSum(nums,target))
>>>>>>> 76109a45cef97d2df776b0b9ea792e1a87a40db8
