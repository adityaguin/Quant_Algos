import math

# There are 100 noodles in a soup bowl you are eating.
# You are blindfolded and told to take the ends of some
# noodles and connect them (each end is chose with equal probability).
# You do this until there are no more free ends.
# What is the expected number of circles created in this fashion?

def recur(i, memo):
    if i in memo:
        return memo[i]
    
    if i == 1:
        memo[1] = 1
        return memo[1]

    ends = 2*i
    possibilities = math.comb(ends, 2)

    # i will give you (1 + f(i-1))

    first = (i / possibilities) * (1 + recur(i-1, memo))
    second = ((possibilities - i) / possibilities) * recur(i-1, memo)
    memo[i] = first + second
    return memo[i] 


if __name__=='__main__':
    print(recur(200, {}))
