def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            s = str(abs(num))
            if s[0] in '13579' and s[-1] in '13579':
                count += 1
    return count