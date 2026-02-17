#w.r.p pyhton function and return a list containing tupes of the form (number, square, cube) for numbers from 1 to 5
def generate_tuples(n):
    result = []
    for i in range(1, n + 1):
        result.append((i, i**2, i**3))
    return result