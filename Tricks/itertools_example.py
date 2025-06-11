from itertools import product

print("Product | ")


def cartesian_product(arr1, arr2):
    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2))


# Driver Function
if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
    print(cartesian_product(arr1, arr2))
print('--------------------------------------------------')
print('islice() and staramp() |')
# Python code to demonstrate the working of
# islice() and starmap()

# importing "itertools" for iterator operations
import itertools

# initializing list
li = [2, 4, 5, 7, 8, 10, 20]

# initializing tuple list
li1 = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]

# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print("The sliced list values are : ", end="")
print(list(itertools.islice(li, 1, 6, 2)))

# using starmap() for selection value acc. to function
# selects min of all tuple values
print("The values acc. to function are : ", end="")
print(list(itertools.starmap(min, li1)))
print('---------------------------------------------------------------------------')
print('takewhile() and tee() |')

# Python code to demonstrate the working of

# importing "itertools" for iterator operations
import itertools

# initializing list
li = [2, 4, 6, 7, 8, 10, 20]

# storing list in iterator
iti = iter(li)

# using takewhile() to print values till condition is false.
print("The list values till 1st false value are : ", end="")
print(list(itertools.takewhile(lambda x: x % 2 == 0, li)))

# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
it = itertools.tee(iti, 3)

# printing the values of iterators
print("The iterators are : ")
for i in range(0, 3):
    print(list(it[i]))
print('---------------------------------------------------------------')
print('zip_longest() |')

# Python code to demonstrate the working of

# importing "itertools" for iterator operations
import itertools

# using zip_longest() to combine two iterables.
print("The combined values of iterables is : ")
print(*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue='_')))
print(' -')

print('product() and permutations()')
# Python code to demonstrate the working of

# importing "itertools" for iterator operations
import itertools

# using product() to print the cartesian product
print("The cartesian product of the containers is : ")
print(list(itertools.product('AB', '12')))

# using permutations to compute all possible permutations
print("All the permutations of the given container is : ")
print(list(itertools.permutations('GfG', 2)))
print('--------------------------------------------------------------------')
print('combination() and combination_with_replacement() |')

# Python code to demonstrate the working of

# importing "itertools" for iterator operations
import itertools

# using combinations() to print every combination
# (without replacement)
print("All the combination of container in sorted order(without replacement) is : ")
print(list(itertools.combinations('1234', 2)))

# using combinations_with_replacement() to print every combination
# with replacement
print("All the combination of container in sorted order(with replacement) is : ")
print(list(itertools.combinations_with_replacement('GfG', 2)))
print('----------------------------------------------------------------')
print('repeat() |')
# Python code to demonstrate the working of
# repeat()

# importing "itertools" for iterator operations
import itertools

# using repeat() to repeatedly print number
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))
print('---------------------------------------------------------------')

# Python program to demonstrate
# iterator module

import operator
import time

# Defining lists
L1 = [1, 2, 3]
L2 = [2, 3, 4]

# Starting time before map
# function
t1 = time.time()

# Calculating result
a, b, c = map(operator.mul, L1, L2)

# Ending time after map
# function
t2 = time.time()

# Time taken by map function
print("Result:", a, b, c)
print("Time taken by map function: %.6f" % (t2 - t1))

# Starting time before naive
# method
t1 = time.time()

# Calculating result using for loop
print("Result:", end=" ")
for i in range(3):
    print(L1[i] * L2[i], end=" ")

# Ending time after naive
# method
t2 = time.time()
print("\nTime taken by for loop: %.6f" % (t2 - t1))

# Python program to demonstrate
# infinite iterators

import itertools

# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")

# Python program to demonstrate
# infinite iterators

import itertools

count = 0

# for in loop
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1

# Python program to demonstrate
# infinite iterators

import itertools

l = ['Geeks', 'for', 'Geeks']

# defining iterator
iterators = itertools.cycle(l)

# for in loop
for i in range(6):
    # Using next function
    print(next(iterators), end=" ")

# Python code to demonstrate the working of
# repeat()

# importing "itertools" for iterator operations
import itertools

# using repeat() to repeatedly print number
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

# import the product function from itertools module
from itertools import product

print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

# import the product function from itertools module
from itertools import permutations

print("All the permutations of the given list is:")
print(list(permutations([1, 'geeks'], 2)))
print()
print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()

print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))

# import combinations from itertools module

from itertools import combinations

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(['A', 2], 2)))
print()

print("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1)))

# import combinations from itertools module

from itertools import combinations_with_replacement

print("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()

print("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2)))
print()

print("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))

# Python code to demonstrate the working of
# accumulate()


import itertools
import operator

# initializing list 1
li1 = [1, 4, 5, 7]

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

# Python code to demonstrate the working of
# and chain()


import itertools

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# using chain() to print all elements of lists
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain(li1, li2, li3)))

# Python code to demonstrate the working of
# chain.from_iterable()


import itertools

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# initializing list of list
li4 = [li1, li2, li3]

# using chain.from_iterable() to print all elements of lists
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain.from_iterable(li4)))

# Python code to demonstrate the working of
# and compress()


import itertools

# using compress() selectively print data values
print("The compressed values in string are : ", end="")
print(list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

# Python code to demonstrate the working of
# dropwhile()


import itertools

# initializing list
li = [2, 4, 5, 7, 8]

# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))

# Python code to demonstrate the working of
# filterfalse()


import itertools

# initializing list
li = [2, 4, 5, 7, 8]

# using filterfalse() to print false values
print("The values that return false to function are : ", end="")
print(list(itertools.filterfalse(lambda x: x % 2 == 0, li)))

print(' ----')
# Python code to demonstrate the working of
# islice()


import itertools

# initializing list
li = [2, 4, 5, 7, 8, 10, 20]

# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print("The sliced list values are : ", end="")
print(list(itertools.islice(li, 1, 6, 2)))

print('-------------------------------------------------------------------------')
# Python code to demonstrate the working of
# starmap()


import itertools

# initializing tuple list
li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]

# using starmap() for selection value acc. to function
# selects min of all tuple values
print("The values acc. to function are : ", end="")
print(list(itertools.starmap(min, li)))

print(' ---')
# Python code to demonstrate the working of
# takewhile()


import itertools

# initializing list
li = [2, 4, 6, 7, 8, 10, 20]

# using takewhile() to print values till condition is false.
print("The list values till 1st false value are : ", end="")
print(list(itertools.takewhile(lambda x: x % 2 == 0, li)))

# Python code to demonstrate the working of
# tee()


import itertools

# initializing list
li = [2, 4, 6, 7, 8, 10, 20]

# storing list in iterator
iti = iter(li)

# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
it = itertools.tee(iti, 3)

# printing the values of iterators
print("The iterators are : ")
for i in range(0, 3):
    print(list(it[i]))

print('-----------------------------------------------------------')
# Python code to demonstrate the working of
# zip_longest()


import itertools

# using zip_longest() to combine two iterables.
print("The combined values of iterables is : ")
print(*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue='_')))

print('---------------------------------------------------------------------')
