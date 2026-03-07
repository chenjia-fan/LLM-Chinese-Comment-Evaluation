def exchange(lst1, lst2):
    odd1 = sum(1 for x in lst1 if x % 2 != 0)
    even2 = sum(1 for x in lst2 if x % 2 == 0)
    return "YES" if odd1 <= even2 else "NO"