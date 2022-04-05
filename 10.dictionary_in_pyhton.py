# key valur pairs named as dictionary here
d1 = ()
print(type(d1))
d2= {}  # THiS will print as dictionary
print(type(d2))
d2 = {"h":"burger","rohan":"ramp",
      "raja":"rain", "shubham":{"uddachiR":"gnd","night":"bedtime"}}
print(d2)
print(d2["h"])
d2["AnkiT"]="kababs"
d2[456]= 'HADDIHIHADDI'
d2.update({"leena":"tofee"})
print(d2["shubham"])
#  removing from the dict
del d2[456]
print(d2)
# while copying the data using assignment operator cause change in original file also
# using the .copy cannot upadate the value in the original file
d3=d2
del d3["h"]
print(d3)
d4 = d2.copy()
del d4["rohan"]
# / what did the output of d4
print(d4)
print(d2)
#  to print the keys
print(d2.keys())
