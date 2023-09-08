p=int(input("please enter value for p:"))
Q=int(input("please enter value for q:"))
# To swap the value of two variables
# we will user third variable which is a temporary variable
temp_1 = p
p = Q
Q = temp_1
print ("The value of p after swapping:",p)
print ("The value of Q after swapping:",Q)