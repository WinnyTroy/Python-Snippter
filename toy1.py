# Create a function that gets the sum of all the digits in a list given as a parameter


n = str([10, 40, 90, 130, 4677907654])
total = 0
def sum(n):
    for x in n:
        for m in str(x):
            # total = sum(int(m))
            total = total + int(m)
    return total
print sum(total)
