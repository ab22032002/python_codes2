grocery = ["xyz","abc","deo",56]
print(grocery)
print(grocery[2])
print(grocery[3])
numbers = [1,331,34,2,4,2,442]
print(numbers[4])
numbers.sort() # to make the array sorted
print(numbers)
numbers.reverse() # to make the number reverse
print(numbers)
print(numbers[0:5])
print(numbers[:4])
print(numbers[:])
# slicing returns a list
print(numbers[::1])
print(numbers[::-1]) # reveersing again
# only one upthere it will only help
# len can be used here to get the length of the string similiar to that
print(len(numbers))
print(max(numbers))
print(min(numbers))
#  appending into the list
numbers.append(79)
print(numbers)
numbers.insert(4,67)
print(numbers)
numbers.remove(2)
print(numbers)
#  removed the first 2 from the list
numbers.pop()
# removes the last element
print(numbers)
#  changing the first value from here mutating the list
numbers[3]=800
print(numbers)
''' immutable -- list 
    touple '''
tp =(1,2,3)
print(tp)
# tp[1] = 40 # cannot assign value to the touple
# print(tp)
#  making the single element touple
tp2 =(1,)
# not giving it a comma wil not print the toupl
print(tp2)
# swappin in python
a=90
b=98
print(a,b)
a,b = b,a
print(a,b)
# use the internet to explore the other functions in python



