def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    indexed_nums = list(enumerate(nums))
    indexed_nums.sort(key=lambda x: (digit_sum(x[1]), x[0]))
    return [num for _, num in indexed_nums]