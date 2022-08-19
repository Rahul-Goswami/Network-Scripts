num = int(input())

# our code
for itr in range(1, num+1):
    x=[itr for inner_itr in range(itr)]
    for itr in x: print(itr, end="")
    print("")