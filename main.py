from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    for i in range(len(nums)):
        
        dif = target - nums[i]
        
        if dif in nums[i+1:]: # if answer exists
            return [i, nums[i+1:].index(dif) + i + 1]
            # return first and second index
            # second index creates sublist and get the index of the sublist
            # then add the initial offset(i+1)

    return # no answer, return None

print(twoSum([2, 7, 11, 15], 9))
