def permute(nums):
    ans = []
    queue = [([], 0, 0)]
    while queue:
        arr_ans, length, start = queue.pop(0)
        if length == 3:
            ans.append(arr_ans)

            for i in range(start, len(nums)):
                num = nums[i]
                queue.append((arr_ans + [num], length + 1, i))
    return ans
ans = permute([1,2,3])
print(ans)