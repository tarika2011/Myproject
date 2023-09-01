# def sum(l):
#     x = 0
#     for i in l:
#         x = x + i
#     return x
#
#
# n=sum([1,2,3,4,5])
# print(n)

# find the largest element in the list

# def largest(n):
#     l = n[0]
#     for i in n:
#
#         if n > l:
#             l = n
#     return l
#
#
# n= largest([10,9,3,14,5])
# print(n)

# Find a python program to reverse a list

# def reverse_list(list):
#
#     list.reverse()
#     return list
#
#
# n = reverse_list([1, 2, 3, 4])
# print(n)

# find a python program to remove all the duplicates from given string python

def remove_duplicate(s1):

    l1=list(s1)
    set1=set(l1)
    print(set1)

remove_duplicate("Hello")

#sum of values in dictionary

def mysum(d1):
    s1=sum(d1.values())

    return s1

dict={'a':10,'b':10,'c':20}
x=mysum(dict)
print(x)