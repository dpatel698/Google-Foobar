def answer(x, y):
    # your code here
    vertical_sum = 1 + sum(range(y))
    if x > 1:
        horizontal_sum = sum(range(y + 1, (y + x)))
    else:
        horizontal_sum = 0

    print(vertical_sum)
    print(horizontal_sum)
    return str(vertical_sum + horizontal_sum)

