def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    elif x % 10 >= 1 and x % 10 < 5:
        return int((x // 10) * 10 + 5)
    elif x % 10 >= 6 and x % 10 < 10:
        return int((x // 10 + 1) * 10)

closest_higher_mod_5(40)
