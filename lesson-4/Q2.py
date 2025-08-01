# WAP to accept mark of 6 student and display then in sorted manner.

mark=[]
user=int(input("enter 1st mark: "))
mark.append(user)

user1=int(input("enter 2nd mark: "))
mark.append(user1)

user2=int(input("enter 3th mark: "))
mark.append(user2)

user3=int(input("enter 4th mark: "))
mark.append(user3)

user4=int(input("enter 4th mark: "))
mark.append(user4)

user5=int(input("enter 5th mark: "))
mark.append(user5)

user6=int(input("enter 6th mark: "))
mark.append(user6)

mark.sort()
print(mark)