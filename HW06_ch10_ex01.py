# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(lst):
    total = 0
    for num in lst:
        if type(num) is list:
            total += nested_sum(num)
        else:
            total += num
    return total

def main():
    pass
    # t = [[1, 2], [3], [4, 5, 6]]
    # u = [[2, 3, 2], [2, 4], [1, 6, 2]]
    # print(nested_sum(u) + nested_sum(t))


if __name__ == '__main__':
    main()