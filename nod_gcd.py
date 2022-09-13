# gcd function copied from https://stackoverflow.com/a/54500627

from itertools import combinations


def gcd(my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


inp_nd = input("Enter number of stories and NOD:")
inp_ai = input("Enter stories importance:")
n, d = [int(i) for i in inp_nd.split()]
ai = [int(i) for i in inp_ai.split()]
for combo in combinations(ai, d):
    nod = gcd(combo)
    if nod != 1:
        print(nod)
        break
