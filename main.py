# Iterate through a list of tuples in Python

my_list = [('a', 'one'), ('b', 'two'), ('c', 'three')]


# a
# one
# b
# two
# c
# three
for tup in my_list:
    for item in tup:
        print(item)