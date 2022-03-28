mystr = "this is string"
#        012345678910111213
#                          -7-6-5-4-3-2-1
print(mystr)
#getting the half part of the  string '
print(mystr[0:8])
# including zero  --- excluding 8
print(mystr[0:13])
print(len(mystr))
# escaping 1 character
print(mystr[0:14:2])
'''
mystr[ :4] // takes bydef as zero for the first value 
mystr[0: ] // takes bydef as length of the string 
mystr[::] // takes one at last and upper cases are satisfied 
'''
print(mystr[::3])
print(mystr[::]) # all the default values here
#  reversing the python string
print(mystr[::-1])
print(type(mystr))
print(mystr.isalnum())
print(mystr.endswith("string")) # true as the last string is string
print(mystr.capitalize())
print(mystr.find("is")) # as the this // contains is
print(mystr.upper()) # to convert the string into the uppercase
print(mystr.replace("is","are"))
# replacing every is by are 
