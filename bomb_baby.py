def answer(M, F):
    # The solution to this problem is to subtract the inputs backwards until they reach M=1 or F=1
    # if this solution cannot be reached then this combination of bombs is impossible. The cycles are counted.
    M, F = int(M), int(F)

    # We evaluate the case where one number of bombs is 1 in which case subtracting 1 from the other type's total
    # gives us the correct answer
    if M == 1:
        return str(F - M)
    elif F == 1:
        return str(M - F)

    cycles = 0
    while M > 0 and F > 0:
        print("M: ", M, "F: ", F)

        # Depending on which bomb type has a greater number we decrement the "distance" between the numbers so
        # the distance is how many times M or F can divide into one another. This eliminates computationally expensive
        # iterations where we subtract the same amount from either M or F
        if M >= F:
            distance = int(M / F)
            M -= F * distance
            cycles += distance

        elif F > M:
            distance = int(F / M)
            F -= M * distance
            cycles += distance

    if not(M == 1 or F == 1):
        return 'impossible'
    else:
        return str(cycles - 1)  # The loop over counts cycles by one each time so we subtract from the final solution
