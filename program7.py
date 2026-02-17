#sum element of list recursively (assume homegenous list )
#min/max of list recursively (assume homegenous list )
a = [1, 2, 3, 4, 5]

def listsummer(a: list[int], ind: int):
    if ind == len(a):
        return 0
    return a[ind] + listsummer(a, ind + 1)

def minelement(a: list[int], ind: int):
    if ind == len(a) - 1:
        return a[ind]
    return min(a[ind], minelement(a, ind + 1))

def maxelement(a: list[int], ind: int):
    if ind == len(a) - 1:
        return a[ind]
    return max(a[ind], maxelement(a, ind + 1))

print("Sum:", listsummer(a, 0))
print("Min:", minelement(a, 0))
print("Max:", maxelement(a, 0))
