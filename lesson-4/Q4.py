# WAP to sum a list with 4 numbers.

number=[12,43,21,34]
a=[12,43,6]*3 #multiple 3time

b=[0]*3 #mulitiply the list
b[0]+=1 # 0 index is replaced by 1

added=sum(number)

print(added)
print(a)
print(b)

