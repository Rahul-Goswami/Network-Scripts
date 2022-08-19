num = int(input())

# our code
for itr in range(1, num+1):
    for inner_itr in range(itr):
        print(itr, end="")
    print("")

