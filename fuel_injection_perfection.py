def answer(n):
    # The operations available to us for the fuel control mechanism is adding a pellet, removing a pellet, and
    # dividing the number of pellets by 2 (when there is an even amount)

    # A method to find the minimum operations to reach 1 pellet is to apply operations until that number is reached
    # and maximize the amount of times we divide by two while minimizing adding/removing pellets
    n = int(n)
    steps = 0
    while n > 1:
        if n == 3:
            n -= 2
            return steps + 2
        if n % 2 == 0:
            n /= 2
            steps += 1
        elif (n - 1) / 2 % 2 == 0:
            n -= 1
            steps += 1
        elif (n + 1) / 2 % 2 == 0:
            n += 1
            steps += 1
        else:
            n -= 1
            steps += 1
    return steps


def find_min_branch(all_ops, find_min, flush_ind):
    while not any(filter(lambda x: x[0] == 1, all_ops)):
        if flush_ind == find_min:
            all_ops = [min(all_ops, key=lambda x: x[0])]
            flush_ind = 0
        new_ops = []
        for i in all_ops:
            if i[0] % 2 == 0:
                new_ops.append((i[0] / 2, i[1] + 1))
            new_ops.append((i[0] + 1, i[1] + 1))
            new_ops.append((i[0] - 1, i[1] + 1))
        all_ops += new_ops
        flush_ind += 1
    return min(filter(lambda x: x[0] == 1, all_ops), key=lambda x: x[1])[1]