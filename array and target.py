

def target_num(nums,target):
  for i in range (len(nums)):
    c=target-nums[i]
    if c in nums:
     print(f"[{nums.index(c),i}]")


print (target_num([2,7,11,15],9))


    