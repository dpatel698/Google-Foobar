def answer(start, length):
    # Iterate through all the ids in the given start and length and calculate the checksum at the spots where
    # the security guards check (Every length worker groups and 1 less at each step)
    checksum = 0
    # The amount of workers not checked
    dec = 0
    # Tracks the amount of ids taken from each line
    chunk_size = length - dec
    # The current id
    i = start
    while dec < length:
        # Compute the checksum on ids in the chunk meaning in the next length amount of workers compute only
        # chunk_size workers ids into the checksum
        if chunk_size > 0:
            checksum ^= xor_range(i, (i + chunk_size) - 1)  # Compute the current chunk xor
            i += chunk_size - 1                             # Skip to the last value in the range
            chunk_size = 0

        else:
            dec += 1  # Increase the amount of workers not checked per line
            i += dec
            chunk_size = length - dec

    return checksum


def xor_range(x, y):
    """
    To optimize the answer function instead of computing the xor of all the ids one by one we can take advantage of
    a pattern that arises when xoring numbers in sequence. That is if you start at a number x and xor the next 3 numbers
    the result is zero and the next 2 is x + 1 and the next one is 1. So the pattern is [x, 1, x+1, 0] repeating in
    the same cycle.
    :param x: the first value in the xor range
    :param y: the last value in the xor range
    :return: the xor of the values in the range [x,y]
    """
    # First we make a function to calculate the xor up from 0 to n
    xor = lambda z: [z, 1, z + 1, 0][z % 4]  # The value determines the xor value in the cycle of 4

    # We xor the next two values because the xor of all the numbers up until [x, y] which is the range we want are
    # included in xor(y) so xor(x - 1) cancels the values we don't need leaving the desired range
    return xor(y) ^ xor(x - 1)
