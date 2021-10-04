from typing import List
a = [3,2,4,3]


def twoSum(nums: List[int], target: int) -> List[int]:
    return [nums.index(i) for i in nums if(target-i) in nums and nums.index(target-i) !=  nums.index(i)]


print(twoSum(a, 6))
