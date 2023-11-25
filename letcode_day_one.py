def twonum(nums,target):
    read_num = {}
    for i , num in enumerate(nums):
        diff = target - num
        if diff in read_num:
            return (read_num[diff],i)
        read_num[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
a = list(twonum(nums, target))
print (a)