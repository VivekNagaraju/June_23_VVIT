'''
1. Define: using [], built-fn 'list'
2. I can create empty list
3. Access: index, slicing operators
4. reverse list: using -1 as step in slicing operator
5. Lists accept duplicate values
6. List is heterogeneous 
7. List is mutable- we can't store fixed objects in a list

Exercises:
1. Count the occurance of each element in a given list
'''
a=[1, 2, 3, 4, 2.0, 1, 3,  2, 4]
# b=[]
c=list(range(6))
weedays=["Mon","Tue",""]
print(a)
# print(b)
# print(c)
# print(a[0]) #index
# print(c[0:5:2]) #slicing operators
# print(c[::-1])
# a[2]=9 # modifiying the list
# print(a)

# print(len(a))
# print(a.count(1))

'''Iterating over list'''
# for x in a:
#     print(x)

# a.append(10)
# print(a)
# a.append(c) # adding the entire list as single element
# print(a)
# print(a[10])
# print(a[11])
# a.insert(4, 99)
# print(a)
# d=a.copy()
# print(d)
a.extend(c)
print(a)
# print(a[11])
b=[]
for x in a:
    if x%2 == 0:
        b.append(x)
print("Normal method:",b)

'''List Comprehension'''
b=[x for x in a if x%2 == 0]
print("List comprehension:", b)


