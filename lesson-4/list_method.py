# there are different types of list method
# list is changable

# sort- update
# reversed 
# append - like push
# insert - add value but it need (index, edited_value)
# pop - delete element in which index
# remove - delete value

# () inside the bracket are called parameter 


list=[3,6,6,53,66,34]

list.sort()    #[3, 6, 6, 34, 53, 66]
list.reverse()   #[34, 66, 53, 6, 6, 3]
list.insert(3,33)     #[3, 6, 6, 33, 53, 66, 34]
list.append(56)     #[3, 6, 6, 53, 66, 34, 56]
list.pop(5)     #[3, 6, 6, 53, 66]
list.remove(53)     #[3, 6, 6, 66, 34]
print(list)

