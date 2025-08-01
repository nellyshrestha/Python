# tuple cant be changed like list
# tuple should altist have 2 or more data
#  to declare tuple it need to be in()
# count(value) , index(value), len() , min() , max()

tuple_eg=(1,3,53,53,"jsgdj","jgdjwh")
tuple_same=(4,32,34,4,23,54)


print(type(tuple_eg))
print(tuple_eg.count(53))   #takes value not index
print(tuple_eg.index("jsgdj"))


print(min(tuple_same))
print(max(tuple_same))    #need to be same data type
print(len(tuple_same))
