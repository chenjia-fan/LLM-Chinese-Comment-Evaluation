def largest_smallest_integers(lst):
    neg_nums = [x for x in lst if x < 0]
    pos_nums = [x for x in lst if x > 0]
    
    max_neg = max(neg_nums) if neg_nums else None
    min_pos = min(pos_nums) if pos_nums else None
    
    return (max_neg, min_pos)