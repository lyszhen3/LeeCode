
  
def removeDuplicates(nums):
    if len(nums) == 0:
       return 0
    j = 0
    for index in range(1,len(nums),1):
        if nums[index] != nums[j]:
           j += 1
           nums[j] = nums[index],
    return j+1
if __name__ == "__main__":
   nums = [1,1,1,2,3,4]
   print(removeDuplicates(nums))
