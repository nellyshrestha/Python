#Syntax:
# variable[started_index : end_index]
# variable[-started_index : -end_index]
# variable[started_index : -end_index]
# variable[-started_index : end_index]


name= "nelly"

print (len(name)) # len= to find length
print(name[2:4]) #  take 
print (name[1:]) # take all length from index 1 to end
print (name[:4]) #take all index from o to given length
print(name)
print(name[-1:5])
print(name[0:-3])

# to skip  index or values
# syntax => var[started_index : end_index : skip_value]

name="samanaisgood"
print(name[0:10:3])