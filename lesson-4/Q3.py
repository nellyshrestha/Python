# check that a tuple type cannot be changed in python.

tuple_eg=(3,45,53,3)
tuple_eg1=(32,54,64)

tuple_eg[1]=5  #tuple cant be added
a=tuple_eg+tuple_eg1 #identifier can be added so tuple can 

print(tuple_eg)
print(a)