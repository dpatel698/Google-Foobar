def answer(xs):
    # your code here
    # xs is a list that contains integers
    # answer(xs) outputs the maximum product of a subset of xs

    # To find the solution we will take the max of the absolute values of xs
    # as the next member of the product and choose to include that member in
    # the product based on whether the solution fulfills the solution output
    # criteria
    next_member = max(xs)
    max_product = next_member
    xs.remove(next_member)
    while xs:
        print(xs)
        next_member = max(xs, key=lambda x: abs(x))
        xs.remove(next_member)
        if abs(max_product) * abs(next_member) > max_product:
            if next_member < 0:
                if any(filter(lambda x: x < 0, xs)) or max_product < 0:
                    max_product *= next_member
            else:
                max_product *= next_member

    return str(max_product)
